# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def LDS(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    LDS Instruction:
    Opcode: 6C
    Action: Implement the specific behavior for LDS.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    address = int(memory_line[2:], 16)

    value = int(memory.load(address), 16)

    registers.S = value

    registers.S &= 0xFFFFFF
