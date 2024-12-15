import os
from typing import Dict

instructions: Dict[str, str] = {
    "18": "ADD",
    "1C": "SUB",
    "20": "MUL",
    "24": "DIV",
    "90": "ADDR",
    "98": "MULR",
    "9C": "DIVR",
    "94": "SUBR",
    "40": "AND",
    "44": "OR",
    "28": "COMP",
    "A0": "COMPR",
    "00": "LDA",
    "68": "LDB",
    "50": "LDCH",
    "08": "LDL",
    "6C": "LDS",
    "74": "LDT",
    "04": "LDX",
    "0C": "STA",
    "78": "STB",
    "54": "STCH",
    "14": "STL",
    "7C": "STS",
    "84": "STT",
    "10": "STX",
    "3C": "J",
    "30": "JEQ",
    "34": "JGT",
    "38": "JLT",
    "48": "JSUB",
    "4C": "RSUB",
    "AC": "RMO",
    "A4": "SHIFTL",
    "A8": "SHIFTR",
    "2C": "TIX",
    "B8": "TIXR",
    "B4": "CLEAR",
}

output_dir: str = "./tiny_tiny_computer/machine/instructions"
test_output_dir: str = "./tests/instructions"

reserved_keywords = {"AND", "OR"}


def sanitize_name(mnemonic: str) -> str:
    """
    Ensure that reserved Python keywords (e.g., 'AND', 'OR') are renamed for module compatibility.
    """
    return (
        f"{mnemonic.lower()}_instruction"
        if mnemonic.upper() in reserved_keywords
        else mnemonic.lower()
    )


def generate_instruction_files(
    instructions: Dict[str, str], output_dir: str, test_dir: str
) -> None:
    """
    Generate individual Python files for each instruction and corresponding test files.
    """
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    for opcode, mnemonic in instructions.items():
        sanitized_name = sanitize_name(mnemonic)  # Handle reserved keywords

        file_path: str = os.path.join(output_dir, f"{sanitized_name}.py")
        with open(file_path, "w") as f:
            f.write(
                f"""# Generated Template From gen.py
                    
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers
                    
def {mnemonic}(memory_line: str, memory: Memory, registers: Registers) -> None:
    \"\"\"
    {mnemonic} Instruction:
    Opcode: {opcode}
    Action: Implement the specific behavior for {mnemonic}.
    :param memory_line: The raw instruction line from memory.
    :param memory: Memory instance to access or store values.
    :param registers: Registers instance to manipulate CPU registers.
    \"\"\"
    raise NotImplementedError("{mnemonic} instruction not implemented yet.")
"""
            )

        test_file_path: str = os.path.join(test_dir, f"test_{sanitized_name}.py")
        with open(test_file_path, "w") as tf:
            tf.write(
                f"""# Auto-generated test case for {mnemonic}
import pytest
from tiny_tiny_computer.machine.instructions.{sanitized_name} import {mnemonic}
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers

def test_{sanitized_name}():
    # Initialize Memory and Registers
    memory = Memory(size_in_words=32)
    registers = Registers()

    # Setup test-specific data
    memory.store(10, "000005")  # Load a test value at address 10
    registers.A = 10  # Set accumulator (A) to an initial value
    registers.PC = 0  # Set the program counter

    # Define the instruction to be tested
    memory_line = "{opcode}" + "000A"  # Example: Opcode {opcode} + address 000A (hex for 10)

    try:
        # Call the instruction
        {mnemonic}(memory_line, memory, registers)

        # Assertions to check expected results (you'll refine this as per logic)
        assert registers.A == 15, "Accumulator should contain the sum of initial A and memory[10]"
    except NotImplementedError:
        pytest.fail("{mnemonic} is not implemented yet.")
"""
            )
    print("Instruction stubs and test cases generated successfully!")


if __name__ == "__main__":
    generate_instruction_files(instructions, output_dir, test_output_dir)
