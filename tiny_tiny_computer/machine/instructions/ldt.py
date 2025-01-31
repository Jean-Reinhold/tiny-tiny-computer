# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def LDT(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    LDT Instruction:
    Opcode: 74
    Action: Implement the specific behavior for LDT.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    address = int(memory_line[2:], 16)

    value = int(memory.load(address), 16)

    registers.T = value

    registers.T &= 0xFFFFFF
