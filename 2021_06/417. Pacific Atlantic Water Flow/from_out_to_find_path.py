from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        max_row = len(heights) - 1
        max_col = len(heights[0]) - 1
        
        
        pacific_out = deque()
        atlantic_out = deque()
        
        for i in range(len(heights)):
            pacific_out.append((i, 0))
            atlantic_out.append((i, max_col))
        
        for i in range(len(heights[0])):
            pacific_out.append((0, i))
            atlantic_out.append((max_row, i))
            
        def find_the_root(q):
            visited, result = set(q), set()
            
            while q:
                g = q.popleft()
                visited.add(g)
                
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_row, new_col = g[0] + x, g[1] + y
                    if not ((new_row, new_col) in visited) and 0 <= new_row <= max_row and 0 <= new_col <= max_col and heights[g[0]][g[1]] <= heights[new_row][new_col]:
                            q.append((new_row, new_col))
            
            return visited
                    
        
        root_of_pacific = find_the_root(pacific_out)
        root_of_atlantic = find_the_root(atlantic_out)
        return list(root_of_pacific & root_of_atlantic)
