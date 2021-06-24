class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def dfs(row, col, count):
            if row < 0 or row == m or col < 0 or col == n:
                return 1
            if count == maxMove:
                return 0
            next_count = count + 1
            return dfs(row - 1, col, next_count) +\
                   dfs(row + 1, col, next_count) +\
                   dfs(row, col - 1, next_count) +\
                   dfs(row, col + 1, next_count)
            
        return dfs(startRow, startColumn, 0) % 1000000007
        
        
