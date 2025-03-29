# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def DIV(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    DIV Instruction:
    Opcode: 24
    Action: Implement the specific behavior for DIV.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    address = int(memory_line[2:], 16)

    value = int(memory.load(address), 16)

    if value == 0:
        raise ZeroDivisionError("Attempted to divide by zero")

    registers.A //= value

    registers.A &= 0xFFFFFF
