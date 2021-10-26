class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dp(current, only_front, full_count):
            if full_count == n:
                result.append(current)
                return
            
            if only_front < n:
                dp(current + "(", only_front + 1, full_count)
                
            if only_front > full_count:
                dp(current + ")", only_front, full_count + 1)
        
        
        dp("", 0, 0)
        
        return result
            
