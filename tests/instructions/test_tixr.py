# Auto-generated test case for TIXR
import pytest

from tiny_tiny_computer.machine.instructions.tixr import TIXR
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_tixr():
    # Initialize Memory and Registers
    memory = Memory(size_in_words=32)
    registers = Registers()

    # Setup test-specific data
    memory.store(10, "000005")  # Load a test value at address 10
    registers.A = 10  # Set accumulator (A) to an initial value
    registers.PC = 0  # Set the program counter
    registers.X = 10
    registers.S = 5

    # Define the instruction to be tested
    memory_line = "B8" + "0004"  # Example: Opcode B8 + address 000A (hex for 10)

    try:
        # Call the instruction
        TIXR(memory_line, memory, registers)

        # Assertions to check expected results (you'll refine this as per logic)
        assert (
            registers.SW == 1
        ), "Status Word should be 1, as registers.X + 1 is greather than registers[r1] (value = 5)"
    except NotImplementedError:
        pytest.fail("TIXR is not implemented yet.")
