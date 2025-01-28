# Auto-generated test case for COMP
import pytest

from tiny_tiny_computer.machine.instructions.comp import COMP
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_comp():
    # Initialize Memory and Registers
    memory = Memory(size_in_words=32)
    registers = Registers()

    # Setup test-specific data
    memory.store(10, "000005")  # Load a test value at address 10
    registers.A = 10  # Set accumulator (A) to an initial value
    registers.PC = 0  # Set the program counter

    # Define the instruction to be tested
    memory_line = "28" + "000A"  # Example: Opcode 28 + address 000A (hex for 10)

    try:
        # Call the instruction
        COMP(memory_line, memory, registers)

        # Assertions to check expected results (you'll refine this as per logic)
        assert (
            registers.SW == 1
        ), "Accumulator should contain [-1] if less, [0] if equal or [1] if greater than memory[10]"
    except NotImplementedError:
        pytest.fail("COMP is not implemented yet.")
