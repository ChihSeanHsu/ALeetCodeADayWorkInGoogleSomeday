class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = len(nums)
        idx = 0
        while last > idx:
            if nums[idx] == val:
                nums[idx] = nums[last - 1]
                last -= 1
            else:
                idx += 1
        return last
