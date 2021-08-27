class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = 0
        for idx in range(len(nums)):
            if nums[curr] != nums[idx]:
                curr += 1
                nums[curr] = nums[idx]
        
        return curr + 1
