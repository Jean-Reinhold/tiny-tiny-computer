            START   1000

; ------------------------------------------------------
; Exemplo de macro recursiva: COUNTDOWN
; Ela tenta reduzir &N até zero, MAS, em tempo de macro-
; expansão, isso não tem efeito real (não há if/else).
; Cada chamada "COUNTDOWN &N" chama a mesma macro de
; novo, gerando um loop infinito na fase de expansão!
; ------------------------------------------------------

MACRO
COUNTDOWN &N
    LDA &N       ; Carrega &N
    COMP #0      ; Compara com 0
    JEQ FIM      ; Se fosse execução real, sairia.
                 ; MAS essa checagem não afeta o
                 ; expand macro, pois é em tempo de execução.

    SUB &N, #1    ; Supondo que &N fosse subtraído em tempo de execução.
                  ; Em tempo de macro, não muda nada.

    COUNTDOWN &N  ; CHAMADA RECURSIVA: expande de novo (loop infinito!)
FIM NOP
MEND

; Simples dados
NUM     WORD 5

MAIN    NOP
        COUNTDOWN NUM  ; Chamada a macro recursiva
        RSUB

            END MAIN
