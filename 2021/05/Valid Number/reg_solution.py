import re

class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = r"[+-]?((\d+\.?\d*)|(\d*\.?\d+))([eE][+-]?\d+)?"
        return re.fullmatch(pattern, s)

    
