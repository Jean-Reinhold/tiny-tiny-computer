# Auto-generated test case for ADDR
import pytest

from tiny_tiny_computer.machine.instructions.addr import ADDR
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_addr():
    # Initialize Memory and Registers
    memory = Memory(size_in_words=32)
    registers = Registers()

    # Setup test-specific data
    registers.PC = 0  # Set the program counter
    registers.X = 10
    registers.A = 5

    # Define the instruction to be tested
    # Example: Opcode 90 + registers A and X (00, 01)
    memory_line = "90" + "0001"

    try:
        # Call the instruction
        ADDR(memory_line, memory, registers)

        # Assertions to check expected results (you'll refine this as per logic)
        assert (
            registers.X == 15
        ), "Accumulator should contain the sum of initial A and memory[10]"
    except NotImplementedError:
        pytest.fail("ADDR is not implemented yet.")
