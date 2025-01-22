# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def STL(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    STL Instruction:
    Opcode: 14
    Action: Implement the specific behavior for STL.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    address = int(memory_line[2:], 16)  # Convert 4-character hex address to int
    value = registers.L
    memory.store(address, f"{value:06X}")
