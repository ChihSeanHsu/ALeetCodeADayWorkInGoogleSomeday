class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        now = 1
        count = 1
        # Pigeonhole principle: times we looping will not exceed K. we cannot meet same remainder after modulo 
        for i in range(1, K + 1):
            r = now % K
            if r == 0:
                return count
            now = now * 10 + 1
            count += 1
        return -1
                
