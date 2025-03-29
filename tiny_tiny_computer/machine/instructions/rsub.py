# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def RSUB(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    RSUB Instruction:
    Opcode: 4C
    Action: Implement the specific behavior for RSUB.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    registers.PC = registers.L

    registers.PC &= 0xFFFFFF
