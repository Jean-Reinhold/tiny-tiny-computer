OLDER   CONST   0
OLD     CONST   1
NEW     CONST   0
LIMIT   CONST   100
LOOP    CONST   5
        ADD     OLDER
        STA     NEW
        LDA     NEW
        COMP    LIMIT
        JGT     FINAL
        LDA     OLD
        STA     OLDER
        LDA     NEW
        STA     OLD
        J      LOOP
FINAL   STOP
        END