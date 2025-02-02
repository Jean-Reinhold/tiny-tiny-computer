# Auto-generated test case for DIVR
import pytest

from tiny_tiny_computer.machine.instructions.divr import DIVR
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_divr():
    # Initialize Memory and Registers
    memory = Memory(size_in_words=32)
    registers = Registers()

    # Setup test-specific data
    memory.store(10, "000005")  # Load a test value at address 10
    registers.A = 5  # Set accumulator (A) to an initial value
    registers.PC = 0  # Set the program counter
    registers.X = 10

    # Define the instruction to be tested
    memory_line = "9C" + "0001"  # Example: Opcode 9C + address 000A (hex for 10)

    try:
        # Call the instruction
        DIVR(memory_line, memory, registers)

        # Assertions to check expected results (you'll refine this as per logic)
        assert (
            registers.X == 2
        ), "X should contain the result of registers[r2] / registers[r1]"
    except NotImplementedError:
        pytest.fail("DIVR is not implemented yet.")
