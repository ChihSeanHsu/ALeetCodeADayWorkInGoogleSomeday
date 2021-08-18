from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = dict(Counter(t))
        met = defaultdict(int)
        # Because there is sorting problem for dict in python before 3.7, we need to use this count to make sure we have met char count we want.
        required_char_count = len(required)
        met_char_count = 0
        
        l, r = 0, 0
        ans = float("inf"), l, r
        while r < len(s):
            char = s[r]
            
            met[char] += 1
            if char in required and required[char] == met[char]:
                met_char_count += 1
            
            # if it meet condition, it's going to shrink from left side.
            while l <= r and required_char_count == met_char_count:
                char = s[l]
                
                met[char] -= 1
                if char in required and required[char] > met[char]:
                    met_char_count -= 1
                
                if ans[0] > r - l + 1:
                    ans = r - l + 1, l, r
                
                l += 1
            
            r += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
