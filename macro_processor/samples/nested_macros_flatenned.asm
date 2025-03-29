START 1000



A RESW 1 ; Storage for variable A
B RESW 1 ; Storage for variable B
C RESW 1 ; Storage for variable C

MAIN LDA A ; Load A into Accumulator
STA B ; Store it in B

LDA A ; Load A
ADD C ; Add the C
STA B ; Store to B
LDA B ; Load B
ADD C ; Add the C
STA A ; Store to A

; A nested macro definition inside SHIFT:
CLEAR &LOC
LDA #0
STA &LOC

; Use the nested macro
CLEAR A
LDA B ; Load B
ADD A ; Add the C
STA C ; Store to C

RSUB ; End of program logic

END MAIN
