START 1000


FIRST WORD 42 ; Arbitrary initial value
SECOND WORD 100
TEMP RESW 1 ; Reserve a word for temporary storage

MAIN NOP
LDA FIRST ; Load from FIRST
STA TEMP ; Store into TEMP
LDA TEMP ; Load from TEMP
STA SECOND ; Store into SECOND
RSUB

END MAIN
