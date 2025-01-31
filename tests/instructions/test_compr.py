# Auto-generated test case for COMPR
import pytest

from tiny_tiny_computer.machine.instructions.compr import COMPR
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_compr():
    # Initialize Memory and Registers
    memory = Memory(size_in_words=32)
    registers = Registers()

    # Setup test-specific data
    registers.A = 10  # Set accumulator (A) to an initial value
    registers.PC = 0  # Set the program counter
    registers.X = 5

    # Define the instruction to be tested
    memory_line = "A0" + "0001"  # Example: Opcode A0 + address 000A (hex for 10)

    try:
        # Call the instruction
        COMPR(memory_line, memory, registers)

        # Assertions to check expected results (you'll refine this as per logic)
        assert (
            registers.SW == 1
        ), "Status Word (SW) should contain [-1] if less, [0] if equal or [1] if greater than r2"
    except NotImplementedError:
        pytest.fail("COMPR is not implemented yet.")
