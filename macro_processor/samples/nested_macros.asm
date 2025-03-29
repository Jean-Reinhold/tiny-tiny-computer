            START   1000

MACRO
SHIFT &SRC1 &SRC2 &COUNT
    SHIFT2 &SRC1 &SRC2 &COUNT
    SHIFT2 &SRC2 &SRC1 &COUNT

    ; A nested macro definition inside SHIFT:
    MACRO
    CLEAR &LOC
        LDA #0
        STA &LOC
    MEND

    ; Use the nested macro
    CLEAR &SRC1
MEND

MACRO
SHIFT2 &FROM &TO &N
    LDA &FROM      ; Load FROM
    ADD &N         ; Add the COUNT
    STA &TO        ; Store to TO
MEND

A           RESW   1      ; Storage for variable A
B           RESW   1      ; Storage for variable B
C           RESW   1      ; Storage for variable C

MAIN        LDA    A       ; Load A into Accumulator
            STA    B       ; Store it in B

            SHIFT  A B C   ; Macro call: SHIFT with A, B, and C
            SHIFT2 B C A   ; Direct call to SHIFT2

            RSUB            ; End of program logic

            END    MAIN