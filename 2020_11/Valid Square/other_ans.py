from collections import defaultdict
import math

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        length_count = defaultdict(int)
        array = [p1, p2, p3, p4]
        for idx, (x1, y1) in enumerate(array):
            for x2, y2 in array[idx+1:]:
                length = math.sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2))
                length_count[length] += 1
                
        for v in length_count.values():
            if (v == 2 or v == 4) and len(length_count) == 2:
                return True
            else:
                return False
