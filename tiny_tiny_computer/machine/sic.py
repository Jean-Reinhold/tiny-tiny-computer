from assembler import two_pass_assemble
from macro_processor import process_file
from tiny_tiny_computer.machine.instruction_mapper import InstructionMapper
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers


class SICMachine:
    def __init__(
        self,
        memory: Memory,
        registers: Registers,
        instruction_mapper: InstructionMapper,
    ) -> None:
        """
        Initialize the SIC Machine with memory, registers, and instruction mapper.

        :param memory: An instance of Memory to manage program and data.
        :param registers: An instance of Registers to manage CPU registers.
        :param instruction_mapper: An instance of InstructionMapper to map opcodes to instructions.
        """
        self.memory: Memory = memory
        self.registers: Registers = registers
        self.instruction_mapper: InstructionMapper = instruction_mapper

    def load_program(self, program: list[str], start_address: int = 0) -> None:
        """
        Load a program into memory starting at a specified address.

        :param program: A list of hexadecimal instruction strings.
        :param start_address: The memory address to start loading the program (default is 0).
        """
        self.memory.load_program(program, start_address)
        self.registers.PC = start_address

    def run(self) -> None:
        """
        Run the program loaded into memory using the fetch-decode-execute cycle.
        """
        while True:
            pc: int = self.registers.PC
            memory_line: str = self.memory.load(pc)

            if memory_line == "000000":  # HALT instruction
                break

            opcode: str = memory_line[
                :2
            ]  # Extract the first two characters as the opcode
            instruction = self.instruction_mapper.get_instruction(opcode)
            instruction(memory_line, self.memory, self.registers)

            # TODO: Check what happens if this is a jump instruction
            self.registers.PC += 1  # Increment program counter to the next instruction

    def step(self) -> None:
        """
        Execute a single step of the program (fetch-decode-execute cycle).
        This method is intended for stepping through the program one instruction at a time.
        """
        pc: int = self.registers.PC
        memory_line: str = self.memory.load(pc)
        print(f"******** Linha da memória: {memory_line} ********")

        if memory_line == "000000":  # HALT instruction
            return  # Program halted

        opcode: str = memory_line[:2]  # Extract the first two characters as the opcode
        instruction = self.instruction_mapper.get_instruction(opcode)
        instruction(memory_line, self.memory, self.registers)

        self.registers.PC += 1  # Increment program counter to the next instruction

    def reset(self):
        for register in vars(self.registers):
            setattr(self.registers, register, 0)

        for i in range(len(self.memory.memory)):
            self.memory.store(i, "000000")
