# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def SHIFTR(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    SHIFTR Instruction:
    Opcode: A8
    Action: Implement the specific behavior for SHIFTR.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    r1 = registers.register_from_code(int(memory_line[2:4], 16))
    n = int(memory_line[4:], 16)
    registers[r1] >>= n
    registers[r1] &= 0xFFFFFF  # Mask to keep the value within 24 bits
