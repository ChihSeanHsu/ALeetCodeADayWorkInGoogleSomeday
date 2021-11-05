class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ""
        n = len(s)
        interval = (numRows - 1) * 2
        for row in range(numRows):
            for idx in range(i, n, interval):
                result += s[idx]
                if row != numRows - 1 and row != 0 and idx + interval - 2 * row < n:
                    result += s[idx + interval - 2 * row]
            
        return result
