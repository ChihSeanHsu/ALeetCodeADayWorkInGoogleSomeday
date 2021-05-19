class Solution:
    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    # for loop
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = [i for i in self.mapping[digits[0]]]
        for d in digits[1:]:
            tmp = []
            for s in self.mapping[d]:
                for i in result:
                    tmp.append(i + s)
            
            result = tmp
        return result
    
    # recursion
    def letterCombinations(self, digits: str) -> List[str]:
        
        ans = []
        def helper(idx, arr=[]):
            
            if idx == len(digits):
                if arr:
                    ans.append("".join(arr))
                
                return
            
            for s in self.mapping[digits[idx]]:
                helper(idx + 1, arr + [s])
                
        helper(0)
        return ans
