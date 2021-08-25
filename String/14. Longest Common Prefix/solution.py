class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        idx = 0
        less_length = float("inf")
        for s in strs:
            less_length = min(less_length, len(s))
        while True and idx < less_length:
            same_prefix = True
            char = strs[0][idx]
            for s in strs[1:]:
                if char != s[idx]:
                    same_prefix = False
                    break
                
            if not same_prefix:
                break
            
            result += char
            idx += 1
        
        return result
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while s.find(prefix) != 0:
                prefix = prefix[:-1]
                if prefix == "":
                    return prefix
        return prefix
