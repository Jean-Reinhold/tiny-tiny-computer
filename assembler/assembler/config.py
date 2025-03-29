MNEMONICS = {
    "ADD": 0x18,
    "SUB": 0x1C,
    "MUL": 0x20,
    "DIV": 0x24,
    "COMP": 0x28,
    "JEQ": 0x30,
    "JGT": 0x34,
    "JLT": 0x38,
    "J": 0x3C,
    "AND": 0x40,
    "OR": 0x44,
    "JSUB": 0x48,
    "RSUB": 0x4C,
    "LDA": 0x50,
    "LDCH": 0x54,
    "LDL": 0x58,
    "LDX": 0x5C,
    "STA": 0x0C,
    "STCH": 0x64,
    "STL": 0x68,
    "STX": 0x6C,
    "RD": 0xD8,
    "WD": 0xDC,
    "TD": 0xE0,
    "BR": 0x00,
    "BRNEG": 0x05,
    "BRPOS": 0x01,
    "BRZERO": 0x04,
    "READ": 0x0C,
    "WRITE": 0x08,
    "STOP": 0x0B,
    "COPY": 0x0D,
    "CALL": 0x0F,
    "RET": 0x10,
}

DIRECTIVES = {"SPACE": 1, "CONST": 1, "START": 1, "END": 0}

MAX_LINE_LEN = 80
MAX_TOKENS = 5

ERRORS = {
    1: "Linha excede tamanho ou número de tokens.",
    2: "Instrução não reconhecida.",
    3: "Operando inválido.",
    4: "Rótulo duplicado.",
    5: "Falta diretiva END para o START.",
    6: "Arquivo de entrada não encontrado.",
    7: "Erro ao escrever arquivo de saída.",
}
