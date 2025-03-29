# Auto-generated test case for STL
import pytest

from tiny_tiny_computer.machine.instructions.stl import STL
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_stl():
    memory = Memory(size_in_words=32)
    registers = Registers()

    registers.L = 10

    memory_line = "14" + "000A"

    try:
        STL(memory_line, memory, registers)

        assert memory.load(10) == "00000A", "memory should be set to 10"
    except NotImplementedError:
        pytest.fail("STA is not implemented yet.")
