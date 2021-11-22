class Solution:
    # Bottom-up
    def minCost(self, costs: List[List[int]]) -> int:
        prev = [0, 0, 0]
        for c_idx, cost in enumerate(costs, 1):
            new_cost = [0, 0, 0]
            for p_idx, price in enumerate(cost):
                new_cost[p_idx] = price + min(prev[:p_idx] + prev[p_idx + 1:])
            prev = new_cost
        return min(prev)
    
    # Top-down
    def minCost(self, costs: List[List[int]]) -> int:
        memo = [[-1, -1, -1] for _ in range(len(costs) + 1)]
        def dfs(cost_idx, prev):
            if cost_idx >= len(costs):
                return 0
            minima_cost = float("inf")
            for idx, price in enumerate(costs[cost_idx]):
                if prev == idx:
                    continue

                if memo[cost_idx + 1][idx] != -1:
                    next_cost = memo[cost_idx + 1][idx]
                else:
                    next_cost = dfs(cost_idx + 1, idx)
                    memo[cost_idx + 1][idx] = next_cost
                
                curr_cost = next_cost + price
                minima_cost = min(curr_cost, minima_cost)
            
            return minima_cost
                
        return dfs(0, -1)
