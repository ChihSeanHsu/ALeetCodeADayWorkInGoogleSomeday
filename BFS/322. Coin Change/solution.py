from collections import deque

class Solution:
    # c=bfs
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        queue = deque([(0, 0)])
        seen = [True] + [False] * amount
        while queue:
            val, count = queue.popleft()
            next_count = count + 1
            for coin in coins:
                next_val = val + coin
                if next_val == amount:
                    return next_count
                elif next_val < amount and not seen[next_val]:
                    seen[next_val] = True
                    queue.append((next_val, next_count))
            
                    
        return -1

    # dp
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("inf")] * amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[-1] if dp[-1] != float("inf") else -1
