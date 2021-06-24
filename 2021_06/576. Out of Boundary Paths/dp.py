class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        M = 1000000007
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[startRow][startColumn] = 1
        result = 0
        
        for move in range(maxMove):
            tmp = [[0 for _ in range(n)] for _ in range(m)]
            for row in range(len(dp)):
                for col in range(len(dp[row])):
                    if row == 0:
                        result = (result + dp[row][col]) % M
                    if row == m - 1:
                        result = (result + dp[row][col]) % M
                    if col == 0:
                        result = (result + dp[row][col]) % M
                    if col == n - 1:
                        result = (result + dp[row][col]) % M
                    
                    up_and_down = ((dp[row - 1][col] if row > 0 else 0) + (dp[row + 1][col] if row < m - 1 else 0)) % M
                    left_and_right = ((dp[row][col - 1] if col > 0 else 0) + (dp[row][col + 1] if col < n - 1 else 0)) % M
                    tmp[row][col] = (up_and_down + left_and_right)
                    
            dp = tmp
        
        return result
                    
                    
        
        
