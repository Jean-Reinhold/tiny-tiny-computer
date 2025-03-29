import importlib
import os


class InstructionMapper:
    def __init__(self):
        self.instructions = {}
        self.load_instructions()

    def load_instructions(self):
        instructions_dir = "tiny_tiny_computer.machine.instructions"
        base_path = os.path.join("tiny_tiny_computer", "machine", "instructions")

        for filename in os.listdir(base_path):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_name = filename[:-3]  # Remove .py
                opcode = self.get_opcode(module_name.upper())
                module = importlib.import_module(f"{instructions_dir}.{module_name}")
                self.instructions[opcode] = getattr(module, module_name.upper(), None)

    def get_opcode(self, mnemonic):
        opcode_map = {
            "ADD": "18",
            "SUB": "1C",
            "MUL": "20",
            "DIV": "24",
            "COMP": "28",
            "JEQ": "30",
            "JGT": "34",
            "JLT": "38",
            "J": "3C",
            "AND": "40",
            "OR": "44",
            "JSUB": "48",
            "RSUB": "4C",
            "LDA": "50",
            "LDCH": "54",
            "LDL": "58",
            "LDX": "5C",
            "STA": "0C",
            "STCH": "64",
            "STL": "68",
            "STX": "6C",
            "RD": "D8",
            "WD": "DC",
            "TD": "E0",
        }
        return opcode_map.get(mnemonic, None)

    def get_instruction(self, opcode):
        if opcode in self.instructions:
            return self.instructions[opcode]
        else:
            raise ValueError(f"Unknown opcode: {opcode}")
