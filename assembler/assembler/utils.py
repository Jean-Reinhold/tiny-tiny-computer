import re
from typing import List

from assembler.config import DIRECTIVES, ERRORS, MAX_LINE_LEN, MAX_TOKENS, MNEMONICS


def is_label(token: str) -> bool:
    return (token not in MNEMONICS) and (token not in DIRECTIVES)


def validate_line(line: str, tokens: List[str]) -> bool:
    if len(line) > MAX_LINE_LEN or len(tokens) > MAX_TOKENS:
        return False
    return True


def log_error(errors: List[str], code: int, extra="") -> None:
    msg = ERRORS.get(code, "Erro desconhecido")
    if extra:
        msg += " - " + extra
    errors.append(msg)
