# Auto-generated test case for MULR
import pytest

from tiny_tiny_computer.machine.instructions.mulr import MULR
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_mulr():
    # Initialize Memory and Registers
    memory = Memory(size_in_words=32)
    registers = Registers()

    # Setup test-specific data
    registers.A = 10  # Set accumulator (A) to an initial value
    registers.X = 5  # Set X to an initial value

    # Define the instruction to be tested
    memory_line = "98" + "0001"  # Example: Opcode 98 + registers A and X

    try:
        # Call the instruction
        MULR(memory_line, memory, registers)

        # Assertions to check expected results (you'll refine this as per logic)
        assert registers.X == 50, "X should contain A (10) * X (5)"
    except NotImplementedError:
        pytest.fail("MULR is not implemented yet.")
