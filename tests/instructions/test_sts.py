# Auto-generated test case for STS
import pytest

from tiny_tiny_computer.machine.instructions.sts import STS
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_sts():
    memory = Memory(size_in_words=32)
    registers = Registers()

    registers.S = 10

    memory_line = "7C" + "000A"

    try:
        STS(memory_line, memory, registers)

        assert memory.load(10) == "00000A", "memory should be set to 10"
    except NotImplementedError:
        pytest.fail("STA is not implemented yet.")
