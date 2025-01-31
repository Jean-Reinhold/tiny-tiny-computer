# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def TIX(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    TIX Instruction:
    Opcode: 2C
    Action: Implement the specific behavior for TIX.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    address = int(memory_line[2:], 16)

    value = int(memory.load(address), 16)

    registers.X += 1

    registers.X &= 0xFFFFFF

    if registers.X < value:
        registers.SW = -1
    elif registers.X == value:
        registers.SW = 0
    else:
        registers.SW = 1

    registers.SW &= 0xFFFFFF
