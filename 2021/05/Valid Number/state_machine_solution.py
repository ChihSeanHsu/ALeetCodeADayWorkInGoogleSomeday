import re

class Solution:
    """
    """
    def isNumber(self, s: str) -> bool:
        START = 0
        POSI = 1
        DIGIT = 2
        DOT = 3
        DIGIT_AFTER_DOT = 4
        EXP = 5
        POSI_AFTER_EXP = 6
        DIGIT_AFTER_EXP = 7
        
        state = START
        flag = False
        for i in s:
            if i.isdigit():
                flag = True
                if state <= DIGIT:
                    state = DIGIT
                elif state == DOT or state == DIGIT_AFTER_DOT:
                    state = DIGIT_AFTER_DOT
                elif state >= EXP:
                    state = DIGIT_AFTER_EXP
            elif i == "+" or i == "-":
                if state == START:
                    state = POSI
                elif state == EXP:
                    state = POSI_AFTER_EXP
                else:
                    return False 
            elif i == ".":
                if state < DOT:
                    state = DOT
                else:
                    return False
            elif i == "e" or i == "E":
                if (state == DOT and flag) or state == DIGIT_AFTER_DOT or state == DIGIT:
                    state = EXP
                else:
                    return False
            else:
                return False
            
        return (
            state == DIGIT or 
            (flag and state == DOT) or
            state == DIGIT_AFTER_DOT or
            state == DIGIT_AFTER_EXP
        )
        
        
