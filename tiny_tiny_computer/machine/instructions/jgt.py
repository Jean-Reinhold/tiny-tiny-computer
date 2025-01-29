# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def JGT(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    JGT Instruction:
    Opcode: 34
    Action: Implement the specific behavior for JGT.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    # Extract the addres from the memory line (assuming the address is in hex format)
    address = int(memory_line[2:], 16)

    # Check if the accumulator is greater than zero
    if registers.CC == '>':
        # Set the program counter to the address
        registers.PC = address
    
