from numpy import ceil, sum as _sum, array

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lower, upper = 1, max(nums)
        nums_array = array(nums)
        while lower < upper:
            mid = (lower + upper) >> 1
            res = _sum(ceil(nums_array / mid))
            if res > threshold:
                lower = mid + 1
            else:
                upper = mid
                
        return lower
