            START   1000

MACRO
MOVE &SRC &DST
    LDA &SRC    ; Load from &SRC
    STA &DST    ; Store into &DST
MEND

FIRST   WORD    42      ; Arbitrary initial value
SECOND  WORD    100
TEMP    RESW    1       ; Reserve a word for temporary storage

MAIN    NOP
        MOVE FIRST TEMP
        MOVE TEMP SECOND
        RSUB

            END MAIN