from collections import Counter

class Solution:
    def maxPower(self, s: str) -> int:
        connect = 1
        cursor = None
        result = 0
        for i in s:
            if i == cursor:
                connect += 1
            else:
                if connect > result:
                    result = connect
                cursor = i
                connect = 1
        else:
            if connect > result:
                result = connect
            
        return result
