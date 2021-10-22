from collections import defaultdict
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        mapping = defaultdict(int)
        max_heap = []
        for i in s:
            mapping[i] += 1
        
        for k, v in mapping.items():
            heapq.heappush(max_heap, (-v, k))
        
        result = ""
        while max_heap:
            v, k = heapq.heappop(max_heap)
            result += k * -v
        return result
