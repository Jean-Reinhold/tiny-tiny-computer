import os
import re
import sys


class ModuleSymbol:
    def __init__(
        self, name: str, value: int, is_extern: bool = False, is_export: bool = False
    ):
        self.name = name
        self.value = value
        self.is_extern = is_extern
        self.is_export = is_export


class ModuleReference:
    def __init__(
        self, symbol_name: str, address: int, byte_offset: int = 2, size: int = 4
    ):
        self.symbol_name = symbol_name
        self.address = address
        self.byte_offset = byte_offset
        self.size = size


class Module:
    def __init__(self, name: str):
        self.name = name
        self.code = []
        self.symbols = {}
        self.references = []
        self.start_address = 0
        self.size = 0
        self.exports = set()
        self.externs = set()

    def add_symbol(
        self, name: str, value: int, is_extern: bool = False, is_export: bool = False
    ):
        self.symbols[name] = ModuleSymbol(name, value, is_extern, is_export)
        if is_extern:
            self.externs.add(name)
        if is_export:
            self.exports.add(name)

    def add_reference(self, symbol_name: str, address: int):
        self.references.append(ModuleReference(symbol_name, address))

    def __str__(self):
        return f"Module {self.name}: {len(self.code)} instructions, {len(self.symbols)} symbols"


class Linker:
    def __init__(self, load_address: int = 0):
        self.modules = []
        self.global_symbol_table = {}
        self.load_address = load_address
        self.final_code = []

    def add_module(self, module: Module):
        self.modules.append(module)

    def parse_object_file(self, filename: str):
        module = Module(os.path.basename(filename))

        try:
            address_pattern = re.compile(
                r"^([0-9A-F]{4})\s+(.+?)(?:\s*;.*)?$", re.IGNORECASE
            )
            const_pattern = re.compile(
                r"^(\w+)\s+CONST\s+([0-9A-F]+)(?:\s*;.*)?$", re.IGNORECASE
            )
            extern_pattern = re.compile(r"^\s*EXTERN\s+(\w+)", re.IGNORECASE)
            export_pattern = re.compile(r"^\s*EXPORT\s+(\w+)", re.IGNORECASE)
            label_pattern = re.compile(r"^(\w+)\s+(.+?)(?:\s*;.*)?$", re.IGNORECASE)

            with open(filename, "r") as file:
                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    if not line or line.startswith(";"):
                        continue

                    extern_match = extern_pattern.match(line)
                    if extern_match:
                        symbol = extern_match.group(1)
                        module.add_symbol(symbol, 0, is_extern=True)
                        continue

                    export_match = export_pattern.match(line)
                    if export_match:
                        symbol = export_match.group(1)
                        if symbol in module.symbols:
                            module.symbols[symbol].is_export = True
                            module.exports.add(symbol)
                        else:
                            print(
                                f"Warning: Exporting undefined symbol {symbol} in {filename}:{line_num}"
                            )
                        continue

                    const_match = const_pattern.match(line)
                    if const_match:
                        symbol = const_match.group(1)
                        value = int(const_match.group(2), 16)
                        module.add_symbol(symbol, value)
                        continue

                    address_match = address_pattern.match(line)
                    if address_match:
                        address = int(address_match.group(1), 16)
                        instruction = address_match.group(2)
                        module.code.append((address, instruction))

                        if address >= module.size:
                            module.size = address + 1
                        continue

                    label_match = label_pattern.match(line)
                    if label_match:
                        label = label_match.group(1)
                        rest = label_match.group(2)
                        if rest.upper() in ["END"]:
                            continue

                        address = len(module.code)
                        module.add_symbol(label, address)
                        continue

            self.add_module(module)
            print(
                f"Parsed module {module.name}: {len(module.code)} instructions, {len(module.symbols)} symbols"
            )
            return True

        except Exception as e:
            print(f"Error parsing {filename}: {e}")
            return False

    def load_module(self, filename: str):
        return self.parse_object_file(filename)

    def first_pass(self):
        current_address = self.load_address

        for module_index, module in enumerate(self.modules):
            module.start_address = current_address

            for symbol_name, symbol in module.symbols.items():
                if symbol.is_extern:
                    continue

                abs_address = current_address + symbol.value

                if symbol_name in self.global_symbol_table:
                    print(f"Warning: Symbol '{symbol_name}' defined multiple times")

                self.global_symbol_table[symbol_name] = (module_index, abs_address)
                symbol.value = abs_address

            current_address += module.size

        for module_index, module in enumerate(self.modules):
            for extern_name in module.externs:
                if extern_name not in self.global_symbol_table:
                    print(
                        f"Error: Unresolved external symbol '{extern_name}' in module {module.name}"
                    )
                    return False

        return True

    def second_pass(self):
        self.final_code = []

        for module_index, module in enumerate(self.modules):
            module_offset = module.start_address

            for addr, instr in module.code:
                new_addr = addr + module_offset
                self.final_code.append((new_addr, instr))

        self.final_code.sort(key=lambda x: x[0])
        return True

    def write_output(self, output_file: str):
        try:
            with open(output_file, "w") as file:
                for address, instruction in self.final_code:
                    file.write(f"{address:04X} {instruction}\n")
            return True
        except Exception as e:
            print(f"Error writing output file: {e}")
            return False

    def link(self, output_file: str):
        """Link all modules and produce the output file."""
        print(f"Linking {len(self.modules)} modules...")

        if not self.first_pass():
            print("First pass failed")
            return False

        if not self.second_pass():
            print("Second pass failed")
            return False

        if not self.write_output(output_file):
            print("Failed to write output file")
            return False

        print(f"Linked program written to {output_file}")
        return True

    def print_summary(self):
        print("\nLinking Summary:")
        print(f"Load address: 0x{self.load_address:04X}")
        print(f"Number of modules: {len(self.modules)}")

        total_size = 0
        for i, module in enumerate(self.modules):
            print(f"Module {i+1}: {module.name}")
            print(f"  Start address: 0x{module.start_address:04X}")
            print(f"  Size: {module.size} bytes")
            print(
                f"  Exports: {', '.join(module.exports) if module.exports else 'None'}"
            )
            print(
                f"  External references: {', '.join(module.externs) if module.externs else 'None'}"
            )
            total_size += module.size

        print(f"Total program size: {total_size} bytes")
        print(
            f"Final address range: 0x{self.load_address:04X} - 0x{self.load_address + total_size - 1:04X}"
        )

        print("\nGlobal Symbol Table:")
        for symbol, (module_idx, address) in sorted(self.global_symbol_table.items()):
            print(f"  {symbol}: 0x{address:04X} (Module {module_idx+1})")


def main():
    linker = Linker(load_address=0)

    if not linker.load_module("fib_module1.obj"):
        print("Failed to load module 1")
        return 1
    if not linker.load_module("fib_module2.obj"):
        print("Failed to load module 2")
        return 1

    output_file = "fibonacci_linked.exe"
    if not linker.link(output_file):
        print("Linking failed")
        return 1

    linker.print_summary()

    print("\nFinal executable content:")
    try:
        with open(output_file, "r") as f:
            print(f.read())
    except:
        print("Could not read output file.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
