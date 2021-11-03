import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        heap = []
        result = 0
        m = len(heightMap)
        n = len(heightMap[0])
        seen = set()
        
        # collect border with height and position
        for row in (0, m - 1):
            for col in range(n):
                heapq.heappush(heap, (heightMap[row][col], row, col))
                
        for row in range(m):
            for col in (0, n - 1):
                heapq.heappush(heap, (heightMap[row][col], row, col))
        
        
        while heap:
            height, row, col = heapq.heappop(heap)
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_row = row + x
                new_col = col + y
                if  0 < new_row < m - 1 and 0 < new_col < n - 1 and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    result += max(0, height - heightMap[new_row][new_col])
                    heapq.heappush(heap, (max(height, heightMap[new_row][new_col]), new_row, new_col))
                    
        return result
    
    
    
