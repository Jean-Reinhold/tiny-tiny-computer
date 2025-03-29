import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from tiny_tiny_computer.machine.instruction_mapper import InstructionMapper
from tiny_tiny_computer.machine.memory import Memory
from tiny_tiny_computer.machine.registers import Registers
from tiny_tiny_computer.machine.sic import SICMachine

def main():
    # Initialize the machine components
    memory = Memory(size_in_words=64)  # Size enough for our program
    registers = Registers()
    instruction_mapper = InstructionMapper()
    sic = SICMachine(memory, registers, instruction_mapper)

    print("Initializing memory with constants and variables...")
    # Initialize memory with constants and variables
    memory.store(33, "000000")  # ZERO = 0
    memory.store(34, "000001")  # ONE = 1
    memory.store(35, "000000")  # OLDER = 0
    memory.store(36, "000000")  # OLD = 0
    memory.store(37, "000000")  # NEW = 0
    memory.store(38, "000005")  # LIMIT = 5

    print("\nMemory initialized with:")
    print(f"ZERO (33) = {int(memory.load(33), 16)}")
    print(f"ONE (34) = {int(memory.load(34), 16)}")
    print(f"OLDER (35) = {int(memory.load(35), 16)}")
    print(f"OLD (36) = {int(memory.load(36), 16)}")
    print(f"NEW (37) = {int(memory.load(37), 16)}")
    print(f"LIMIT (38) = {int(memory.load(38), 16)}")

    # Fibonacci program in hex format
    program = [
        # Initialize OLDER = 0
        "500021",  # LDA ZERO (address 33)
        "0C0023",  # STA OLDER (address 35)
        
        # Initialize OLD = 1
        "500022",  # LDA ONE (address 34)
        "0C0024",  # STA OLD (address 36)
        
        # FRONT: LOAD OLDER
        "500023",  # LDA OLDER (address 35)
        
        # ADD OLD
        "180024",  # ADD OLD (address 36)
        
        # STORE NEW
        "0C0025",  # STA NEW (address 37)
        
        # Compare NEW with LIMIT
        "500025",  # LDA NEW (address 37)
        "280026",  # COMP LIMIT (address 38)
        "340020",  # JGT FINAL (address 32)
        
        # COPY OLD to OLDER
        "500024",  # LDA OLD (address 36)
        "0C0023",  # STA OLDER (address 35)
        
        # COPY NEW to OLD
        "500025",  # LDA NEW (address 37)
        "0C0024",  # STA OLD (address 36)
        
        # Jump back to FRONT
        "3C0005",  # J FRONT (address 5)
        
        # FINAL: HALT
        "000000",  # HALT
    ]

    print("\nLoading program into memory...")
    # Load the program into memory
    sic.load_program(program, 0)

    print("\nStarting Fibonacci program execution...")
    print("Initial state:")
    print(f"PC: {sic.registers.PC}")
    print(f"A: {sic.registers.A}")
    print(f"X: {sic.registers.X}")
    print(f"L: {sic.registers.L}")
    print(f"B: {sic.registers.B}")
    print(f"S: {sic.registers.S}")
    print(f"T: {sic.registers.T}")
    print(f"F: {sic.registers.F}")
    print(f"SW: {sic.registers.SW}")
    print("-" * 50)

    # Execute the program step by step
    step_count = 0
    max_steps = 50  # Safety limit to prevent infinite loops
    
    while step_count < max_steps:
        print(f"\nStep {step_count + 1}:")
        print(f"PC: {sic.registers.PC}")
        
        # Print current instruction
        current_instruction = memory.load(sic.registers.PC)
        print(f"Current instruction: {current_instruction}")
        
        # Execute one step
        sic.step()
        
        # Print current state
        print("\nCurrent state:")
        print(f"PC: {sic.registers.PC}")
        print(f"A: {sic.registers.A}")
        print(f"SW: {sic.registers.SW}")
        print(f"OLDER = {int(memory.load(35), 16)}")
        print(f"OLD = {int(memory.load(36), 16)}")
        print(f"NEW = {int(memory.load(37), 16)}")
        print(f"LIMIT = {int(memory.load(38), 16)}")
        print("-" * 50)
        
        step_count += 1
        
        # Check for HALT instruction
        if memory.load(sic.registers.PC) == "000000":
            print("\nHALT instruction reached!")
            break

    print("\nProgram finished!")
    print(f"Final values:")
    print(f"OLDER = {int(memory.load(35), 16)}")
    print(f"OLD = {int(memory.load(36), 16)}")
    print(f"NEW = {int(memory.load(37), 16)}")
    print(f"LIMIT = {int(memory.load(38), 16)}")
    
    print("\nFibonacci sequence generated:")
    sequence = []
    for addr in range(35, 38):  # OLDER, OLD, NEW
        value = int(memory.load(addr), 16)
        if value > 0:
            sequence.append(value)
    print(", ".join(str(x) for x in sequence))

if __name__ == "__main__":
    main() 