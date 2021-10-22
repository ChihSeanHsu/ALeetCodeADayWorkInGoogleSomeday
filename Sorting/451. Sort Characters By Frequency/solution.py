from collections import defaultdict
import heapq

class Solution:    
    def frequencySort(self, s: str) -> str:
        mapping = defaultdict(int)

        for i in s:
            mapping[i] += 1
        
        pairs = sorted(mapping.items(), key=lambda x: x[1], reverse=True)
        
        result = ""
        for k, v in pairs:
            result += k * v
        return result
