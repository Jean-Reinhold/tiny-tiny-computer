# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def JGT(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    JGT Instruction:
    Opcode: 34
    Action: PC ← m if CC > 0
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    # Extract the address from the memory line (assuming the address is in hex format)
    address = int(memory_line[2:], 16)

    print(f"JGT: Checking SW = {registers.SW}")

    # Check if the condition code is greater than 0
    if registers.SW > 0:
        print(f"JGT: Condition met (SW > 0), jumping to address {address}")
        registers.PC = address
    else:
        print(f"JGT: Condition not met (SW <= 0), continuing to next instruction")

    # Update the accumulator with the sum of its initial value and the value at the memory address
    registers.A += int(memory.load(address), 16)
