# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def ADDR(memory_line: str, _: Memory, registers: Registers) -> None:
    """
    ADDR Instruction:
    Opcode: 90
    Action: Implement the specific behavior for ADDR.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """

    # get name of both registers
    r1 = registers.register_from_code(int(memory_line[2:4], 16))
    r2 = registers.register_from_code(int(memory_line[4:], 16))

    # sum register (r1) into register (r2)
    registers[r2] += registers[r1]
