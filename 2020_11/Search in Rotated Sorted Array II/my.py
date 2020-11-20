class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        n = len(nums)
        start = 0
        end = n - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            
            # ex: 7 7 7 1 2 3
            if nums[start] == nums[mid]:
                start += 1
                continue
   
            # [7, 7, 7, 8, 1, 2, 3]
            # |    a     |    b   |
            # check mid and target in a or b
            pivot_array = nums[start] <= nums[mid]
            target_array = nums[start] <= target
            
            # if someone in a or someone in b
            if pivot_array ^ target_array:
                # mid in a
                if pivot_array:
                    start = mid + 1
                # target in a
                else:
                    end = mid - 1
            # both in a or both in b
            else:
                if target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
