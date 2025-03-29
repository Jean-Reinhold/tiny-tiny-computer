import os
from typing import List

from .pass_one import pass_one
from .pass_two import pass_two


def two_pass_assemble(filepath: str) -> bool:
    errors: List[str] = []
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        from .utils import log_error

        log_error(errors, 6)
        for e in errors:
            print(e)
        return False

    symbol_table, line_addresses = pass_one(lines, errors)
    object_code = pass_two(lines, symbol_table, line_addresses, errors)

    has_errors = bool(errors)
    if has_errors:
        for e in errors:
            print("Erro:", e)

    base, _ = os.path.splitext(filepath)
    obj_file = base + ".obj"
    lst_file = base + ".lst"

    try:
        with open(obj_file, "w") as of:
            for code_line in object_code:
                of.write(code_line + "\n")

        with open(lst_file, "w") as lf:
            for i, line in enumerate(lines):
                addr = line_addresses[i]
                txt_addr = f"{addr:04X}" if addr >= 0 else "----"
                lf.write(f"{txt_addr}  {line.strip()}\n")

            if errors:
                lf.write("\nErros encontrados:\n")
                for e in errors:
                    lf.write(e + "\n")
            else:
                lf.write("\nNenhum erro detectado.\n")

    except OSError:
        from .utils import log_error

        log_error(errors, 7)
        return False

    return not has_errors
