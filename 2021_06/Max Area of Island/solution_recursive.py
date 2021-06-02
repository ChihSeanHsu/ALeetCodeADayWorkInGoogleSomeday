class Solution:
    def dfs(self, grid, row, col) -> int:
        count = 0
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1):
            return count
        
        grid[row][col] = 0
        count += 1
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            count += self.dfs(grid, row + x, col + y)
        
        return count
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    result = max(result, self.dfs(grid, row, col))
                    
        return result
        
