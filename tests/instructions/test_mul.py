# Auto-generated test case for MUL
import pytest

from tiny_tiny_computer.machine.instructions.mul import MUL
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_mul():
    # Initialize Memory and Registers
    memory = Memory(size_in_words=32)
    registers = Registers()

    # Setup test-specific data
    memory.store(10, "000005")  # Load a test value at address 10
    registers.A = 10  # Set accumulator (A) to an initial value
    registers.PC = 0  # Set the program counter

    # Define the instruction to be tested
    memory_line = "20" + "000A"  # Example: Opcode 20 + address 000A (hex for 10)

    try:
        # Call the instruction
        MUL(memory_line, memory, registers)

        # Assertions to check expected results (you'll refine this as per logic)
        assert (
            registers.A == 50
        ), "Accumulator should countain A * 0x0A memory (5)"
    except NotImplementedError:
        pytest.fail("MUL is not implemented yet.")
