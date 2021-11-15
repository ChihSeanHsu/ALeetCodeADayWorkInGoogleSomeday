class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[num] for num in nums]
        result_idx = 0
        count = 0
        for idx in range(1, len(nums)):
            curr = []
            for j in range(idx):
                if nums[idx] % nums[j] == 0 and len(curr) < len(dp[j]) + 1:
                    curr = dp[j]
            dp[idx] = curr + [nums[idx]]
            if count < len(dp[idx]):
                result_idx = idx
                count = len(dp[idx])
                
        return dp[result_idx]
            
