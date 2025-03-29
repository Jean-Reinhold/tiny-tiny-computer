# Generated Template From gen.py

from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def COMP(memory_line: str, memory: Memory, registers: Registers) -> None:
    """
    COMP Instruction:
    Opcode: 28
    Action: CC ← (A) : (m..m+2)
    Sets SW to:
    -1 if A < m
    0 if A = m
    1 if A > m
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    """
    address = int(memory_line[2:], 16)
    value = int(memory.load(address), 16)
    
    print(f"COMP: Comparing A ({registers.A}) with memory[{address}] ({value})")
    
    # Ensure we're comparing signed values
    if registers.A < value:
        registers.SW = -1
        print(f"COMP: A < value, setting SW to -1")
    elif registers.A == value:
        registers.SW = 0
        print(f"COMP: A == value, setting SW to 0")
    else:
        registers.SW = 1
        print(f"COMP: A > value, setting SW to 1")
    
    print(f"COMP: Final SW value = {registers.SW}")
