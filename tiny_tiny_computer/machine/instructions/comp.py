# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def COMP(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    COMP Instruction:
    Opcode: 28
    Action: Implement the specific behavior for COMP.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    address = int(memory_line[2:], 16)

    value = int(memory.load(address), 16)

    if registers.A < value:
        registers.SW = -1
    elif registers.A == value:
        registers.SW = 0
    else:
        registers.SW = 1

    registers.SW &= 0xFFFFFF
