# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def JSUB(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    JSUB Instruction:
    Opcode: 48
    Action: Implement the specific behavior for JSUB.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    # Extract the address from the memory line (assuming the address is in hex format)
    address = int(memory_line[2:], 16)

    # Save the return address (current PC + 1) in the link register (assuming L is the link register)
    registers.L = registers.PC + 1

    # Set the program counter to the address
    registers.PC = address

    # Update the accumulator with the sum of its initial value and the value at the memory address
    registers.A += int(memory.load(address), 16)