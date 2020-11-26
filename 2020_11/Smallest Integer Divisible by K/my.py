class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        v = set()
        now = 1
        count = 1
        while True:
            tmp = now % K
            if tmp == 0:
                return count
            else:
                if tmp in v:
                    return -1
                else:
                    v.add(tmp)
                    count += 1
                    now = now * 10 + 1
                
