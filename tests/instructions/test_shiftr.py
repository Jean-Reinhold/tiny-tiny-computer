# Auto-generated test case for SHIFTR
import pytest

from tiny_tiny_computer.machine.instructions.shiftr import SHIFTR
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_shiftr():
    # Initialize Memory and Registers
    memory = Memory(size_in_words=32)
    registers = Registers()

    # Setup test-specific data
    registers.A = 160  # Set accumulator (A) to an initial value
    registers.PC = 0  # Set the program counter

    # Define the instruction to be tested
    memory_line = "A8" + "0004"  # Example: Opcode A8 + register A, and amount 4

    try:
        # Call the instruction
        SHIFTR(memory_line, memory, registers)

        # Assertions to check expected results (you'll refine this as per logic)
        assert registers.A == 10, f"Accumulator should be equal to 10 >> 4 ({10 >> 4})"
    except NotImplementedError:
        pytest.fail("SHIFTR is not implemented yet.")
