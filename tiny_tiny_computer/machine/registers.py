from pydantic import BaseModel


class Registers(BaseModel):
    A: int = 0  # Accumulator
    X: int = 0  # Index register
    L: int = 0  # Linkage register
    B: int = 0  # Base register
    S: int = 0  # General-use register
    T: int = 0  # General-use register
    F: int = 0  # Floating-point accumulator (48 bits)
    PC: int = 0  # Program Counter
    SW: int = 0  # Status Word (CC)

    def register_from_code(self, code: int) -> str:
        register_code_map = {
            0: "A",
            1: "X",
            2: "L",
            3: "B",
            4: "S",
            5: "T",
            6: "F",
        }

        return register_code_map[code]

    def __getitem__(self, key: str) -> int:
        return getattr(self, key)

    def __setitem__(self, key: str, value: int):
        setattr(self, key, value)
