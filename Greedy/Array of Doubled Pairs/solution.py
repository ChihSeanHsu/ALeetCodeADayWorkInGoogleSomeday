from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        for d in sorted(counter, key=abs):
            double = d * 2        
            if counter[double] < counter[d]:
                return False
            counter[double] -= counter[d]
        return True
            
            
