class Memory:
    def __init__(self, size_in_words=32):
        self.memory = ["000000"] * size_in_words

    def load(self, address: int) -> str:
        """Fetch a memory word as a string."""
        return self.memory[address]

    def store(self, address: int, value: str):
        """
        Store a hexadecimal string in memory.
        The value should represent a valid machine word.
        """
        if not isinstance(value, str) or len(value) != 6:
            raise ValueError(
                f"Memory value must be a 6-character hexadecimal string. Got: {value}"
            )
        self.memory[address] = value

    def load_program(self, program: list[str], start_address: int):
        """
        Load a program (hex strings) into memory starting at a given address.
        """
        for i, line in enumerate(program):
            self.store(start_address + i, line)
