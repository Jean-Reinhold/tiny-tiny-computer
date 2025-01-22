# Auto-generated test case for SUBR
import pytest

from tiny_tiny_computer.machine.instructions.subr import SUBR
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_subr():
    # Initialize Memory and Registers
    memory = Memory(size_in_words=32)
    registers = Registers()

    # Setup test-specific data
    registers.X = 10
    registers.A = 5

    # Define the instruction to be tested
    # Example: Opcode 94 + registers A and X (00, 01)
    memory_line = "90" + "0001"

    try:
        # Call the instruction
        SUBR(memory_line, memory, registers)

        # Assertions to check expected results (you'll refine this as per logic)
        assert (
            registers.X == 5
        ), "Accumulator should contain the sum of initial A and memory[10]"
    except NotImplementedError:
        pytest.fail("ADDR is not implemented yet.")
