from typing import Dict, List, Tuple

from assembler.assembler.config import DIRECTIVES, MNEMONICS
from assembler.assembler.utils import is_label, log_error, validate_line


def pass_one(lines: List[str], errors: List[str]) -> Tuple[Dict[str, int], List[int]]:
    symbol_table: Dict[str, int] = {}
    line_addresses: List[int] = []

    lc = 0
    started = False
    end_found = False

    for line_idx, line in enumerate(lines):
        original_line = line.strip()
        if not original_line:
            line_addresses.append(-1)
            continue

        tokens = original_line.split()
        if not validate_line(original_line, tokens):
            log_error(errors, 1, f"na linha {line_idx+1}: {original_line}")
            line_addresses.append(-1)
            continue

        line_addresses.append(lc)

        label = None
        first = tokens[0]
        op_idx = 0
        if is_label(first):
            label = first
            op_idx = 1
            if label in symbol_table:
                log_error(
                    errors, 4, f"na linha {line_idx+1}: rótulo '{label}' duplicado"
                )
            else:
                symbol_table[label] = lc

        # Identifica a operação real (mnemônico ou diretiva)
        if op_idx >= len(tokens):
            continue

        operation = tokens[op_idx]

        if operation == "START":
            started = True
            if op_idx + 1 < len(tokens):
                try:
                    start_val = int(tokens[op_idx + 1])
                    lc = start_val
                    line_addresses[-1] = lc
                except ValueError:
                    pass
            continue

        if operation == "END":
            end_found = True
            # END também não gera instrução (geralmente)
            continue

        # Se for uma diretiva que aloca espaço ou constante
        if operation in ("SPACE", "CONST"):
            lc += 1
            continue

        # Se for um mnemônico
        if operation in MNEMONICS:
            lc += 1
            continue

        log_error(errors, 2, f"na linha {line_idx+1}: '{operation}' não reconhecida")
        lc += 1

    if started and not end_found:
        log_error(errors, 5, "O arquivo acabou mas não encontrou 'END'")

    return (symbol_table, line_addresses)
