# Auto-generated test case for TIX
import pytest

from tiny_tiny_computer.machine.instructions.tix import TIX
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_tix():
    # Initialize Memory and Registers
    memory = Memory(size_in_words=32)
    registers = Registers()

    # Setup test-specific data
    memory.store(10, "000005")  # Load a test value at address 10
    registers.A = 10  # Set accumulator (A) to an initial value
    registers.PC = 0  # Set the program counter
    registers.X = 10

    # Define the instruction to be tested
    memory_line = "2C" + "000A"  # Example: Opcode 2C + address 000A (hex for 10)

    try:
        # Call the instruction
        TIX(memory_line, memory, registers)

        # Assertions to check expected results (you'll refine this as per logic)
        assert (
            registers.SW == 1
        ), "Status Word should be 1, as registers.X + 1 is greather than memory[10] (value = 5)"
    except NotImplementedError:
        pytest.fail("TIX is not implemented yet.")
