class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == 1:
            return max(cardPoints[0], cardPoints[-1])
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)
        
        tmp = sum(cardPoints[:k])
        result = tmp
        for i in range(1, k + 1):
            tmp = tmp - cardPoints[k - i] + cardPoints[-i]
            result = max(result, tmp)
        return result
        
        
