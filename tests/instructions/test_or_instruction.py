# Auto-generated test case for OR
import pytest

from tiny_tiny_computer.machine.instructions.or_instruction import OR
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_or_instruction():
    # Initialize Memory and Registers
    memory = Memory(size_in_words=32)
    registers = Registers()

    # Setup test-specific data
    memory.store(10, "000054")  # Load a value at address 10    0x54   (0b001010100)
    registers.A = 0x84  # Set accumulator (A) to an initial value 0x84 (0b010000100)

    # Define the instruction to be tested
    memory_line = "44" + "000A"  # Example: Opcode 40 + address 000A (hex for 10)

    try:
        # Call the instruction
        OR(memory_line, memory, registers)

        # Assertions to check expected results (you'll refine this as per logic)
        assert (
            registers.A == 212
        ), f"Accumulator should be equal to {0x54 | 0x84}"
    except NotImplementedError:
        pytest.fail("AND is not implemented yet.")
