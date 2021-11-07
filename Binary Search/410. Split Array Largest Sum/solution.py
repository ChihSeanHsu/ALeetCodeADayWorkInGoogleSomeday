"""
We want to find out maxima subarray sum `x` and it must be max(nums) < x < sum(nums), so we can just easily to use binary search to find out x in this range.
And check if maxima is `x` can we split nums in `m` subarrays or not.

It's just a bineary search pattern.
"""

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def is_valid(mid):
            curr_sum = 0
            subarrays = 0
            for i in nums:
                tmp = curr_sum + i
                if tmp > mid:
                    subarrays += 1
                    curr_sum = i
                else:
                    curr_sum = tmp
            subarrays += 1
            return subarrays <= m
        
        left, right = max(nums), sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if is_valid(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
