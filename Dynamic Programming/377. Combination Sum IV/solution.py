from collections import deque

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        queue = deque()
        queue.append(([], target))
        ans = set()
        
        while queue:
            collection, remain = queue.popleft()
            for num in nums:
                curr = remain - num
                new_collection = collection.copy() + [curr]
                if curr > 0:
                    queue.append((new_collection, curr))
                elif curr == 0:
                     ans.add(tuple(new_collection))
        
        return len(ans)
    
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for i in range(1, len(dp)):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        
        return dp[target]
        
        
