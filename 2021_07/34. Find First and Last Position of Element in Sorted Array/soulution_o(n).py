class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]
        
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        result = [-1, -1]
        start = 0
        end = len(nums) - 1
    
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                break
            elif nums[mid] >= target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
        else:
            return result

        
        left, right = mid, mid
        while left > -1 and nums[left] == target:
            left -= 1
        while right < len(nums) and nums[right] == target:
            right += 1

        return [left + 1, right - 1]
