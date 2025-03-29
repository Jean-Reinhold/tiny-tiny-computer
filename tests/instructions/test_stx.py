# Auto-generated test case for STX
import pytest

from tiny_tiny_computer.machine.instructions.stx import STX
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_stx():
    memory = Memory(size_in_words=32)
    registers = Registers()

    registers.X = 10

    memory_line = "10" + "000A"

    try:
        STX(memory_line, memory, registers)

        assert (
            memory.load(10) == "00000A"
        ), "memory should be set to 10"
    except NotImplementedError:
        pytest.fail("STA is not implemented yet.")
