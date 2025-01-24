# Auto-generated test case for STA
import pytest

from tiny_tiny_computer.machine.instructions.sta import STA
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_sta():
    memory = Memory(size_in_words=32)
    registers = Registers()

    registers.A = 10

    memory_line = "0C" + "000A"

    try:
        STA(memory_line, memory, registers)

        assert (
            memory.load(10) == "00000A"
        ), "memory should be set to 10"
    except NotImplementedError:
        pytest.fail("STA is not implemented yet.")
