class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips = ones = 0
        for i in s:
            if i == "0":
                flips += 1
            else:
                ones += 1 
            flips = min(ones, flips)
        return flips
