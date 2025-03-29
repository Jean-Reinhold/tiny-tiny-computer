# Auto-generated test case for STB
import pytest

from tiny_tiny_computer.machine.instructions.stb import STB
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_stb():
    memory = Memory(size_in_words=32)
    registers = Registers()

    registers.B = 10

    memory_line = "0C" + "000A"

    try:
        STB(memory_line, memory, registers)

        assert (
            memory.load(10) == "00000A"
        ), "memory should be set to 10"
    except NotImplementedError:
        pytest.fail("STA is not implemented yet.")
