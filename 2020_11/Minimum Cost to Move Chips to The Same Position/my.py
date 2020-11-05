from collections import Counter
"""
 1. position odd to odd and even to even cost is 0
 2. odd to even or even to odd cost is 1
 3. count how much even or odd is it.
 4. then get minimum
"""
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        counter = Counter(position)
        odd, even = 0, 0
        for k, v in counter.items():
            if k % 2 == 0:
                even += v
            else:
                odd += v
            
        length = len(position)
        return min(odd, even)
        
