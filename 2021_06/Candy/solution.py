class Solution:
    def candy(self, ratings: List[int]) -> int:
        result = [1 for _ in range(len(ratings))]
        
        for idx in range(1, len(ratings)):
            prev = idx - 1
            if ratings[prev] < ratings[idx]:
                result[idx] = result[prev] + 1
                
        
        for idx in range(len(ratings) - 2, -1, -1):
            next_ = idx + 1
            if ratings[next_] < ratings[idx]:
                result[idx] = max(result[idx], result[next_] + 1)
        
        return sum(result)
            
            
