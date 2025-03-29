# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def LDA(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    LDA Instruction:
    Opcode: 50
    Action: A ← (m..m+2)
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    # Extract the address from the memory line (assuming the address is in hex format)
    address = int(memory_line[2:], 16)

    # Load the value from memory into the accumulator
    value = int(memory.load(address), 16)
    registers.A = value

    print(f"LDA: Loaded value {value} from memory[{address}] into A")

    registers.A &= 0xFFFFFF
