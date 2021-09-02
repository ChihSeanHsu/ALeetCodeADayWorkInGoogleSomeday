class Solution:    
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[0] = nums[0]
        for idx in range(1, len(nums)):
            dp[idx] = max(nums[idx], dp[idx - 1] + nums[idx])
        return max(dp)
    
    def maxSubArray(self, nums: List[int]) -> int:
        max_seen = float("-inf")
        max_curr = 0
        for idx in range(len(nums)):
            max_curr += nums[idx]
            max_seen = max(max_seen, max_curr, nums[idx])
            if max_curr < nums[idx]:
                max_curr = nums[idx]
        return max_seen
