# Auto-generated test case for CLEAR
import pytest

from tiny_tiny_computer.machine.instructions.clear import CLEAR
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_clear():
    # Initialize Memory and Registers
    memory = Memory(size_in_words=32)
    registers = Registers()

    # Setup test-specific data
    registers.A = 10  # Set accumulator (A) to an initial value

    # Define the instruction to be tested
    memory_line = "04" + "00"  # Example: Opcode 04 + register 00 (A)

    try:
        # Call the instruction
        CLEAR(memory_line, memory, registers)

        # Assertions to check expected results (you'll refine this as per logic)
        assert (
            registers.A == 0
        ), "Register A must be cleared (set to 0)"
    except NotImplementedError:
        pytest.fail("CLEAR is not implemented yet.")
