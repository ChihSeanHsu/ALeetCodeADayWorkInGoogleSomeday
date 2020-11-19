class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                str_tmp = ''
                while stack and stack[-1] != '[':
                    str_tmp = stack.pop() + str_tmp
                
                # pop out '['
                stack.pop()
                
                num = 0
                base = 1
                while stack and stack[-1].isdigit():
                    num += int(stack.pop()) * base
                    base *= 10
                
                stack.append(str_tmp * num)
  
        
        return ''.join(stack)
        
