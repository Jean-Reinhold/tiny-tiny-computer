# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def STA(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    STA Instruction:
    Opcode: 0C
    Action: (m..m+2) ← A
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    # Extract the address from the memory line (assuming the address is in hex format)
    address = int(memory_line[2:], 16)

    # Store the accumulator value in memory
    value = registers.A & 0xFFFFFF  # Ensure 24-bit value
    memory.store(address, f"{value:06x}")

    print(f"STA: Stored value {value} from A into memory[{address}]")
