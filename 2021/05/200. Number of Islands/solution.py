class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    self.dfs(grid, row, col)
        return count
                    
        
    def dfs(self, grid, row, col):
        if 0 > row or row >= len(grid) or 0 > col or col >= len(grid[0]) or grid[row][col] == "0":
            return
        grid[row][col] = "0"
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            self.dfs(grid, row + i, col + j)
            
