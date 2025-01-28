# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def DIVR(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    DIVR Instruction:
    Opcode: 9C
    Action: Implement the specific behavior for DIVR.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    r1 = registers.register_from_code(int(memory_line[2:4], 16))
    r2 = registers.register_from_code(int(memory_line[4:], 16))

    registers[r2] //= registers[r1]

    registers[r2] &= 0xFFFFFF
