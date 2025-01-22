# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def CLEAR(memory_line: str, _: Memory, registers: Registers) -> None:
    """
    CLEAR Instruction:
    Opcode: 04
    Action: Implement the specific behavior for CLEAR.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    r = registers.register_from_code(int(memory_line[2:], 16))
    registers[r] = 0
