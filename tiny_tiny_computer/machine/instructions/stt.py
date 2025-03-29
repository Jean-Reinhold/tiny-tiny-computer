# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def STT(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    STT Instruction:
    Opcode: 84
    Action: Implement the specific behavior for STT.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    address = int(memory_line[2:], 16)  # Convert 4-character hex address to int
    value = registers.T
    memory.store(address, f"{value:06X}")
