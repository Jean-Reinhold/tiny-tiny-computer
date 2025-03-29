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
    """
    # Extract the address from the memory line (assuming the address is in hex format)
    address = int(memory_line[2:], 16)
    
    # Get the value from memory
    value = int(memory.load(address), 16)
    
    # Add the value to the accumulator
    registers.A = (registers.A + value) & 0xFFFFFF  # Ensure 24-bit result
    
    print(f"ADD: Added {value} to A. New A value: {registers.A}")
