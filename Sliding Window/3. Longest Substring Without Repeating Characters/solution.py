class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        curr = ""
        seen = {}
        start = 0
        end = 0
        while end != len(s):
            c = s[end]
            if c in seen:
                result = max(result, len(curr))
                start = seen[c] + 1
                seen = {}
                curr = ""
                for i in range(start, end + 1):
                    seen[s[i]] = i
                    curr += s[i]
            else:
                curr += c
                seen[c] = end
            end += 1
        return max(result, len(curr))
                
  
  
    # fast but not sliding window
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        curr = ""
        for c in s:
            if c in curr:
                result = max(result, len(curr))
                curr = curr.split(c)[-1] + c
            else:
                curr += c
        return max(result, len(curr))
                
