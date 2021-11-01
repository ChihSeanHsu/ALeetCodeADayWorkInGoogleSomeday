class Solution:
    def decodeString(self, s: str) -> str:
        tmp_num = ""
        num_stack = []
        char_stack = []
        
        result = ""
        for c in s:
            if c.isdigit():
                tmp_num += c
            elif c.isalpha():
                result += c
            elif c == "[":
                num = int(tmp_num)
                num_stack.append(num)
                tmp_num = ""
                char_stack.append(result)
                result = ""
            elif c == "]":
                curr = char_stack.pop()
                for i in range(num_stack.pop()):
                    curr = curr + result
                result = curr
            
        return result
