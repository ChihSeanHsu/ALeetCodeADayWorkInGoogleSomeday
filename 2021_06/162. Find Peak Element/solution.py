class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        def helper(start, end):
            mid = (start + end) // 2
            prev, next_ = mid - 1, mid + 1
            if prev < 0:
                return mid

            if next_ == n:
                if nums[prev] > nums[mid]:
                    return prev
                else:
                    return mid

            if nums[prev] < nums[mid] and nums[next_] < nums[mid]:
                return mid
            
            if nums[prev] == nums[next_]:
                return helper(start, mid) or helper(mid, end)

            if nums[prev] < nums[next_]:
                return helper(mid, end)

            if nums[prev] > nums[next_]:
                return helper(start, mid)
        
        return helper(0, n)
    
    
