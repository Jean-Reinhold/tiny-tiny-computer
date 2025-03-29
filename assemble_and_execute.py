import os
import sys

# Add the project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from tiny_tiny_computer.machine.instruction_mapper import InstructionMapper
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers
from tiny_tiny_computer.machine.sic import SICMachine, load_obj_file, two_pass_assemble


def main():
    memory = Memory(size_in_words=64)
    registers = Registers()
    instruction_mapper = InstructionMapper()
    sic = SICMachine(memory, registers, instruction_mapper)

    program, pc = load_obj_file("sample.obj")

    print("Loaded program:")
    for i, instruction in enumerate(program):
        print(f"{i}: {instruction}")

    sic.load_program(program, 0)
    sic.registers.PC = pc

    print(f"Starting execution at PC = {sic.registers.PC}")

    sic.run()

    print("\nMemory after execution:")
    for i in range(16):  # Print the first 16 memory locations
        print(f"{i}: {memory.load(i)}")

    print("\nProgram finished!")
    print(f"Final values:")
    print(f"OLDER = {int(memory.load(0), 16)}")
    print(f"OLD = {int(memory.load(1), 16)}")
    print(f"NEW = {int(memory.load(2), 16)}")
    print(f"LIMIT = {int(memory.load(3), 16)}")


if __name__ == "__main__":
    two_pass_assemble(filepath="sample.asm")
    main()
