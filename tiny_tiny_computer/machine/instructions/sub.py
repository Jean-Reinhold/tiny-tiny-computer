# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def SUB(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    SUB Instruction:
    Opcode: 1C
    Action: A ← (A) - (m..m+2)
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    # Extract the address from the memory line (assuming the address is in hex format)
    address = int(memory_line[2:], 16)
    
    # Get the value from memory
    value = int(memory.load(address), 16)
    
    # Convert to signed values (24-bit)
    a_signed = registers.A if registers.A < 0x800000 else registers.A - 0x1000000
    value_signed = value if value < 0x800000 else value - 0x1000000
    
    # Subtract the value from the accumulator
    result = a_signed - value_signed
    
    # Convert back to unsigned 24-bit
    registers.A = result & 0xFFFFFF
    
    print(f"SUB: {a_signed} - {value_signed} = {result}")
    print(f"SUB: Result stored in A: {registers.A}")
