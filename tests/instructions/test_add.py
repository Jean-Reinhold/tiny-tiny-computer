import pytest

from tiny_tiny_computer.machine.instructions.add import ADD
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_add():
    memory = Memory(size_in_words=32)
    registers = Registers()

    # Setup test-specific data
    memory.store(10, "000005")  # Store the value 5 at memory address 10
    registers.A = 10  # Set the initial value of the accumulator to 10
    registers.PC = 0  # Program Counter set to 0 (not relevant for this test)

    memory_line = "18000A"  # Opcode 18 (ADD) + address 000A (hex for 10)

    ADD(memory_line, memory, registers)

    assert (
        registers.A == 15
    ), "Accumulator should contain the sum of initial A and memory[10]"
    assert memory.load(10) == "000005", "Memory at address 10 should remain unchanged"
