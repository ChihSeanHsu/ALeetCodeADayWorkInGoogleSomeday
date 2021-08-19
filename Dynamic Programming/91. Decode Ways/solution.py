from collections import deque

class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith("0"):
            return 0
        if len(s) == 1:
            return 1 if s != "0" else 0
        
        dp = [0] * len(s)
        # first ele must be 1~9
        dp[0] += 1
        
        if s[1] != "0":
            dp[1] += dp[0]
        if int(s[0:2]) <= 26:
            dp[1] += 1
        
        for i in range(2, len(s)):
            if s[i] != "0":
                dp[i] += dp[i - 1]
            
            two = s[i - 1:i + 1]
            if not two.startswith("0") and int(two) <= 26:
                dp[i] += dp[i - 2]
                
        return dp[-1]

        
        
