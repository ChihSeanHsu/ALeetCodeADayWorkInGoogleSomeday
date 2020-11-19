class Solution:
    def decodeString(self, s: str) -> str:
        int_stack = []
        str_stack = ['']
        int_tmp = ''
        for i in s:
            if i.isdigit():
                int_tmp += i
            elif i == '[':
                int_stack.append(int(int_tmp))
                int_tmp = ''
                str_stack.append('')
            elif i == ']':
                num = int_stack.pop()
                value = str_stack.pop()
                str_stack[-1] += value * num
            else:
                str_stack[-1] += i
        
        return str_stack[-1]
        
