# Auto-generated test case for STT
import pytest

from tiny_tiny_computer.machine.instructions.stt import STT
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


def test_stt():
    memory = Memory(size_in_words=32)
    registers = Registers()

    registers.T = 10

    memory_line = "84" + "000A"

    try:
        STT(memory_line, memory, registers)

        assert memory.load(10) == "00000A", "memory should be set to 10"
    except NotImplementedError:
        pytest.fail("STA is not implemented yet.")
