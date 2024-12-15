# Auto-generated test case for JSUB
import pytest

from tiny_tiny_computer.machine.instructions.jsub import JSUB
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_jsub():
    # Initialize Memory and Registers
    memory = Memory(size_in_words=32)
    registers = Registers()

    # Setup test-specific data
    memory.store(10, "000005")  # Load a test value at address 10
    registers.A = 10  # Set accumulator (A) to an initial value
    registers.PC = 0  # Set the program counter

    # Define the instruction to be tested
    memory_line = "48" + "000A"  # Example: Opcode 48 + address 000A (hex for 10)

    try:
        # Call the instruction
        JSUB(memory_line, memory, registers)

        # Assertions to check expected results (you'll refine this as per logic)
        assert (
            registers.A == 15
        ), "Accumulator should contain the sum of initial A and memory[10]"
    except NotImplementedError:
        pytest.fail("JSUB is not implemented yet.")
