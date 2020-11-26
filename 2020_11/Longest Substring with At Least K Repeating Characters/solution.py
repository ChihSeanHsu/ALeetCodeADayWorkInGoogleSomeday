
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        for i in set(s):
            if s.count(i) < k:
                return max([self.longestSubstring(j, k) for j in s.split(i)])
            
        return len(s)
