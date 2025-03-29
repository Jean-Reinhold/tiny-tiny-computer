# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def LDB(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    LDB Instruction:
    Opcode: 68
    Action: Implement the specific behavior for LDB.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    address = int(memory_line[2:], 16)

    value = int(memory.load(address), 16)

    registers.B = value

    registers.B &= 0xFFFFFF
