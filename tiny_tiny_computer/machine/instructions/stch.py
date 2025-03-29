# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def STCH(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    STCH Instruction:
    Opcode: 54
    Action: Implement the specific behavior for STCH.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
   # Extract the address from the memory line (last 4 characters)
    address = int(memory_line[2:], 16)

    # Load the value from memory at the specified address
    memory_value = int(memory.load(address), 16)

    # Add the memory value to the accumulator
    registers.A += memory_value