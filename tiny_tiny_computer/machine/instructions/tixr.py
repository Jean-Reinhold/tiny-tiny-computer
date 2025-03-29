# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def TIXR(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    TIXR Instruction:
    Opcode: B8
    Action: Implement the specific behavior for TIXR.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    r1 = registers.register_from_code(int(memory_line[2:4], 16))

    registers.X += 1

    registers.X &= 0xFFFFFF

    if registers.X < registers[r1]:
        registers.SW = -1
    elif registers.X == registers[r1]:
        registers.SW = 0
    else:
        registers.SW = 1

    registers.SW &= 0xFFFFFF
