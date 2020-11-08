from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lower, upper = 1, max(nums)
        ans = []
        while lower < upper:
            mid = (lower + upper) >> 1
            res = 0
            for i in nums:
                res += ceil(i / mid)
            
            if res > threshold:
                lower = mid + 1
            else:
                upper = mid
                
        return lower
