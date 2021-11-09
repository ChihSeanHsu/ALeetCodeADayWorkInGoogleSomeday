from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        prev = 0
        avoid = using = 0
        for k in sorted(counter):
            if k - 1 != prev:
                avoid, using = max(avoid, using), k * counter[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k * counter[k] + avoid
            
            prev = k
            
        return max(avoid, using)
