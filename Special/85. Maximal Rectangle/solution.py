class Solution:
    # dp O(mn*n)
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dp = [[0] * len(matrix[0]) for _ in matrix]
        result = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "0":
                    continue
                width = dp[row][col] = dp[row][col - 1] + 1 if col else 1
            
                for back in range(row, -1, -1):
                    width = min(dp[back][col], width)
                    result = max(result, width * (row - back + 1))
                    
        return result
            
    # stack monotonic stack O(mn)
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        heights = [0] * len(matrix[0])
        def calculate():
            stack = [-1]
            for idx in range(len(heights)):
                while stack[-1] != -1 and heights[stack[-1]] > heights[idx]:
                    self.result = max(self.result, heights[stack.pop()] * (idx - stack[-1] - 1))
                
                stack.append(idx)
            
            while stack[-1] != -1:
                self.result = max(self.result, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        
        self.result = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "0":
                    heights[col] = 0
                else:
                    heights[col] += 1
                
            calculate()
        
        return self.result
