class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for c in s:
            if stack:
                tmp = stack.pop()
                if c != tmp:
                    stack.append(tmp)
                else:
                    continue
            stack.append(c)

        return "".join(stack)
        
