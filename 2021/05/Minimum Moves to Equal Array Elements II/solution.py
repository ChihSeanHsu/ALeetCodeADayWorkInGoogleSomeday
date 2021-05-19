class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        mid = len(nums) // 2
        nums.sort()
        
        result = 0
        for i in nums:
            result += abs(i - nums[mid])
            
        return result
