class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == "(" or p == "{" or p == "[":
                stack.append(p)
                continue
            elif p == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            elif p == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            elif p == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
        return True if not stack else False

    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            "{": "}",
            "(": ")",
            "[": "]",
        }
        for p in s:
            if p in mapping:
                stack.append(p)
            elif stack and mapping[stack[-1]] == p:
                stack.pop()
            else:
                return False
            
        return len(stack) == 0
            
