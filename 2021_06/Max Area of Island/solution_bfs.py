from collections import deque

class Solution:
    def check_valid(self, grid, row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1
    
    def bfs(self, grid, row, col) -> int:
        count = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stack = deque([(row, col)])
        grid[row][col] = 0
        while stack:
            r, c = stack.popleft()
            count += 1
            for x, y in dirs:
                new_row = r + x
                new_col = c + y
                if self.check_valid(grid, new_row, new_col):
                    grid[new_row][new_col] = 0
                    stack.append((new_row, new_col))       

        return count
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    result = max(result, self.bfs(grid, row, col))
                    
        return result
        
