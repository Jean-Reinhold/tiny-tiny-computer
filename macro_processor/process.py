import os
import sys
from collections import defaultdict, deque
from typing import Dict, List, Tuple

from pydantic import BaseModel, Field


class MacroDefinition(BaseModel):
    name: str
    parameters: List[str]
    body: List[str] = Field(default_factory=list)


def parse_macros(lines: List[str]) -> Tuple[List[str], Dict[str, MacroDefinition]]:
    macros: Dict[str, MacroDefinition] = {}
    program_lines: List[str] = []

    inside_macro = False
    macro_level = 0
    current_macro_name = ""
    is_new_macro = False

    for line in lines:
        stripped = line.strip()

        if stripped == "MEND":
            if macro_level > 0:
                macro_level -= 1
                if macro_level == 0:
                    inside_macro = False
            continue

        if stripped.startswith("MACRO"):
            macro_level += 1
            inside_macro = True
            if macro_level == 1:
                is_new_macro = True
            continue

        if inside_macro and macro_level > 0:
            if is_new_macro:
                parts = stripped.split()
                current_macro_name = parts[0]
                params = parts[1:]

                macros[current_macro_name] = MacroDefinition(
                    name=current_macro_name, parameters=params, body=[]
                )
                is_new_macro = False

            else:
                macros[current_macro_name].body.append(stripped)

            continue

        program_lines.append(stripped)

    return program_lines, macros


def expand_program(
    program_lines: List[str], macros: Dict[str, MacroDefinition]
) -> List[str]:
    frames: List[Tuple[List[str], int]] = [(program_lines, 0)]
    param_stacks: Dict[str, deque] = defaultdict(deque)

    expanded_output: List[str] = []

    while frames:
        print(f"Tamanho da pilha: {len(frames)}")
        lines, index = frames[-1]

        if index >= len(lines):
            frames.pop()
            continue

        line = lines[index]
        frames[-1] = (lines, index + 1)

        tokens = line.split()
        if not tokens:
            expanded_output.append(line)
            continue

        macro_name_candidate = tokens[0]
        if macro_name_candidate in macros:
            macro_def = macros[macro_name_candidate]
            real_args = tokens[1:]

            link = _match_params(macro_def.parameters, real_args, param_stacks)

            for formal, real_val in link.items():
                param_stacks[formal].append(real_val)

            frames.append((macro_def.body, 0))
            frames.append(
                (["__END_MACRO_EXPANSION__ " + " ".join(macro_def.parameters)], 0)
            )

        elif line.startswith("__END_MACRO_EXPANSION__"):
            _, *formals = line.split()
            for formal in formals:
                if param_stacks[formal]:
                    param_stacks[formal].pop()
            continue
        else:
            # A normal line: do parameter substitution, then write it out
            substituted = _substitute_params(line, param_stacks)
            expanded_output.append(substituted)

    return expanded_output


def _normalize_param(token: str) -> str:
    if token.startswith("&"):
        return token[1:]
    return token


def _match_params(formals, real_args, param_stacks):
    link = {}
    for i, formal in enumerate(formals):
        normalized_formal = _normalize_param(formal)
        if i < len(real_args):
            candidate = _normalize_param(real_args[i])
            # now 'formal' and 'candidate' are stored without '&'
            link[normalized_formal] = (
                param_stacks[candidate][-1]
                if (candidate in param_stacks and param_stacks[candidate])
                else candidate
            )
        else:
            link[normalized_formal] = "???"
    return link


def _substitute_params(line: str, param_stacks):
    tokens = line.split()
    result = []
    for token in tokens:
        has_amp = token.startswith("&")
        bare = token[1:] if has_amp else token

        if bare in param_stacks and param_stacks[bare]:
            real = param_stacks[bare][-1]
            result.append(real)
        else:
            result.append(token)
    return " ".join(result)


def process_file(input_file: str) -> str:
    base, _ = os.path.splitext(input_file)
    output_file = f"{base}_flatenned.asm"

    with open(input_file, "r", encoding="utf-8") as f_in:
        all_lines = f_in.readlines()

    program_lines, macros = parse_macros(all_lines)
    expanded_lines = expand_program(program_lines, macros)
    with open(output_file, "w", encoding="utf-8") as f_out:
        for line in expanded_lines:
            f_out.write(line + "\n")

    return os.path.abspath(output_file)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python macro_processor.py <input_file>")
        sys.exit(1)

    input_filename = sys.argv[1]
    try:
        output_path = process_file(input_filename)
        print(f"Macro expansion complete. Output written to: {output_path}")
    except Exception as exc:
        print(f"Error while processing macros: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
