from typing import Dict, List

from assembler.config import MNEMONICS
from assembler.utils import is_label, log_error


def pass_two(
    lines: List[str],
    symbol_table: Dict[str, int],
    line_addresses: List[int],
    errors: List[str],
) -> List[str]:
    object_code = []

    for line_idx, line in enumerate(lines):
        original_line = line.strip()
        if not original_line or original_line.startswith("*"):
            continue

        tokens = original_line.split()
        address = line_addresses[line_idx]
        if address < 0:
            continue

        label = None
        op_idx = 0
        first = tokens[0]
        if is_label(first):
            label = first
            op_idx = 1

        if op_idx >= len(tokens):
            continue

        operation = tokens[op_idx]

        if operation in ("START", "END"):
            continue

        if operation == "SPACE":
            object_code.append(f"{address:04X} 00")
            continue

        if operation == "CONST":
            if op_idx + 1 < len(tokens):
                operand_str = tokens[op_idx + 1]
                try:
                    val = int(operand_str)
                    object_code.append(f"{address:04X} {val:02X}")
                except ValueError:
                    log_error(
                        errors,
                        3,
                        f"Operando inválido '{operand_str}' na linha {line_idx+1}",
                    )
            else:
                log_error(
                    errors, 3, f"Faltando operando em CONST na linha {line_idx+1}"
                )
            continue

        if operation in MNEMONICS:
            opcode = MNEMONICS[operation]
            operand_value = 0

            if op_idx + 1 < len(tokens):
                operand = tokens[op_idx + 1]

                if operand.startswith("#"):
                    immediate_str = operand[1:]
                    try:
                        operand_value = int(immediate_str)
                    except ValueError:
                        log_error(
                            errors,
                            3,
                            f"Operando imediato inválido '{operand}' (linha {line_idx+1})",
                        )

                elif is_label(operand):
                    if operand in symbol_table:
                        operand_value = symbol_table[operand]
                    else:
                        log_error(
                            errors,
                            3,
                            f"Label '{operand}' não definido (linha {line_idx+1})",
                        )

                else:
                    try:
                        operand_value = int(operand)
                    except ValueError:
                        log_error(
                            errors,
                            3,
                            f"Operando inválido '{operand}' (linha {line_idx+1})",
                        )

            # Gera código -> [opcode, operand_value]
            assembled = f"{address:04X} {opcode:02X} {operand_value:02X}"
            object_code.append(assembled)
            continue
        pass

    return object_code
