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

    def fetch_instruction(self) -> str:
        """
        Fetch the instruction at the current PC address.
        
        :return: The instruction as a string from memory.
        """
        return self.memory.load(self.registers.PC)

    def decode_instruction(self, instruction: str) -> tuple[str, str]:
        """
        Decode the instruction into opcode and operand.
        
        :param instruction: The instruction string to decode.
        :return: A tuple containing (opcode, operand).
        """
        opcode = instruction[:2]
        operand = instruction[2:]
        return opcode, operand

    def execute_instruction(self, instruction: str) -> None:
        """
        Execute the instruction using the instruction mapper.
        
        :param instruction: The instruction string to execute.
        """
        opcode = instruction[:2]
        instruction_func = self.instruction_mapper.get_instruction(opcode)
        instruction_func(instruction, self.memory, self.registers)

    def run(self) -> None:
        """
        Run the program loaded into memory using the fetch-decode-execute cycle.
        """
        while True:
            # Fetch instruction at current PC
            instruction = self.fetch_instruction()
            
            if instruction == "000000":  # HALT instruction
                break

            # Save current PC
            current_pc = self.registers.PC
            
            # Execute the instruction
            self.execute_instruction(instruction)
            
            # Only increment PC if it wasn't modified by the instruction
            if self.registers.PC == current_pc:
                self.registers.PC += 1
                print(f"PC incrementado automaticamente para: {self.registers.PC}")

    def step(self) -> None:
        """
        Execute a single step of the program (fetch-decode-execute cycle).
        This method is intended for stepping through the program one instruction at a time.
        """
        # Fetch instruction at current PC
        instruction = self.fetch_instruction()
        print(f"******** Linha da memória: {instruction} ********")

        if instruction == "000000":  # HALT instruction
            return  # Program halted

        # Save current PC
        current_pc = self.registers.PC
        
        # Execute the instruction
        self.execute_instruction(instruction)
        
        # Only increment PC if it wasn't modified by the instruction
        if self.registers.PC == current_pc:
            self.registers.PC += 1

    def reset(self):
        for register in vars(self.registers):
            setattr(self.registers, register, 0)

        for i in range(len(self.memory.memory)):
            self.memory.store(i, "000000")
