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
