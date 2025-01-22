from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def ADD(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    ADD Instruction:
    Opcode: 18
    Action: A ← (A) + (m..m+2)
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
 git@github.com:Jean-Reinhold/tiny-tiny-computer.git   """
    address = int(memory_line[2:], 16)  # Convert 4-character hex address to int

    value = int(memory.load(address), 16)  # Memory value is a 6-character hex string

    registers.A += value

    registers.A &= 0xFFFFFF  # Mask to keep the value within 24 bits
