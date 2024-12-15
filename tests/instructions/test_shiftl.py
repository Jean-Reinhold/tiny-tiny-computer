# Auto-generated test case for SHIFTL
import pytest

from tiny_tiny_computer.machine.instructions.shiftl import SHIFTL
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_shiftl():
    # Initialize Memory and Registers
    memory = Memory(size_in_words=32)
    registers = Registers()

    # Setup test-specific data
    memory.store(10, "000005")  # Load a test value at address 10
    registers.A = 10  # Set accumulator (A) to an initial value
    registers.PC = 0  # Set the program counter

    # Define the instruction to be tested
    memory_line = "A4" + "000A"  # Example: Opcode A4 + address 000A (hex for 10)

    try:
        # Call the instruction
        SHIFTL(memory_line, memory, registers)

        # Assertions to check expected results (you'll refine this as per logic)
        assert (
            registers.A == 15
        ), "Accumulator should contain the sum of initial A and memory[10]"
    except NotImplementedError:
        pytest.fail("SHIFTL is not implemented yet.")
