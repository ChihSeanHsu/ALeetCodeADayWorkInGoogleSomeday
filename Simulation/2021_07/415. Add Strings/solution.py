from collections import deque

class Solution:        
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        idx1, idx2 = len(num1) - 1, len(num2) - 1
        carry = 0
        while idx1 >= 0 or idx2 >= 0 or carry > 0:
            
            if idx1 >= 0:
                carry += ord(num1[idx1]) - ord("0")
                idx1 -= 1
            if idx2 >= 0:
                carry += ord(num2[idx2]) - ord("0")
                idx2 -= 1

            result.append(chr(carry % 10 + ord("0")))
            carry //= 10
        
        return "".join(result[::-1])
    
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        idx1, idx2 = len(num1) - 1, len(num2) - 1
        carry = 0
        while idx1 >= 0 or idx2 >= 0 or carry > 0:
            if idx1 >= 0:
                carry += int(num1[idx1])
                idx1 -= 1
            if idx2 >= 0:
                carry += int(num2[idx2])
                idx2 -= 1

            carry, num = divmod(carry, 10)
            result += str(num)
            
        return result[::-1]
