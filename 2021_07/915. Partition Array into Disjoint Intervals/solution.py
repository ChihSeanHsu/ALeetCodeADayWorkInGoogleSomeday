class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = nums[0]
        curr_max = nums[0]
        result = 1
        for i in range(1, len(nums)):
            if left_max > nums[i]:
                result = i + 1
                left_max = curr_max
            else:
                curr_max = max(curr_max, nums[i])
                
        return result
