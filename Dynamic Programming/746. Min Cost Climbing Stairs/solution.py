class Solution:
    # time: O(n), space: O(n)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            cur = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
            dp[i] = cur
        return dp[-1]
    
    # time: O(n), space: O(1)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = cost[0]
        b = cost[1]
        
        for i in range(2, len(cost)):
            b, a = cost[i] + min(a, b), b
        
        return min(a, b)
