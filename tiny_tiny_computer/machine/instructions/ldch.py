# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def LDCH(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    LDCH Instruction:
    Opcode: 50
    Action: Implement the specific behavior for LDCH.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    # Extract the address from the memory line (assuming the address is in hex format)
    address = int(memory_line[2:], 16)

    # Load the value from the memory address
    value = int(memory.load(address), 16)

    # Update the accumulator with the sum of its initial value and the loaded value
    registers.A += value
