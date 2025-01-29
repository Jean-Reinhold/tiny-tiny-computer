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
    # Get the address to jump to (assuming the address is in hex format)
    address = int(memory_line[2:], 16)
    # Save the current program counter to the L register
    registers.L = registers.PC
    # Set the program counter to the address
    registers.PC = address
