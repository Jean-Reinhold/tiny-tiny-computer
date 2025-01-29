# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def JEQ(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    JEQ Instruction:
    Opcode: 30
    Action: Implement the specific behavior for JEQ.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
 # Extract the address from the memory line (assuming the address is in hex format)
    address = int(memory_line[2:], 16)
    
    # Check if the accumulator is zero
    if registers.CC == '=':
        # Set the program counter to the address
        registers.PC = address