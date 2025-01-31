# Auto-generated test case for RMO
import pytest

from tiny_tiny_computer.machine.instructions.rmo import RMO
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_rmo():
    # Initialize Memory and Registers
    memory = Memory(size_in_words=32)
    registers = Registers()

    # Setup test-specific data
    memory.store(10, "000005")  # Load a test value at address 10
    registers.A = 10  # Set accumulator (A) to an initial value
    registers.PC = 0  # Set the program counter
    registers.X = 5

    # Define the instruction to be tested
    memory_line = "AC" + "0001"  # Example: Opcode AC + address 000A (hex for 10)

    try:
        # Call the instruction
        RMO(memory_line, memory, registers)

        # Assertions to check expected results (you'll refine this as per logic)
        assert (
            registers.X == 10
        ), "Registers[r2] should contain the same value as registers[r1]"
    except NotImplementedError:
        pytest.fail("RMO is not implemented yet.")
