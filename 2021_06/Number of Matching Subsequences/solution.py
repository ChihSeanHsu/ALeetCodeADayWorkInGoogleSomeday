class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        result = 0
        for word in words:
            start = 0
            for i in word:
                start = s.find(i, start) + 1
                if not start:
                    break
            else:
                result += 1
                
        return result
                    
        
