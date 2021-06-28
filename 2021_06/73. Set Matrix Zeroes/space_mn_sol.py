class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        stack = []
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    stack.append((row, col))
                    
        
        for x, y in stack:
            for i in range(len(matrix)):
                matrix[i][y] = 0
                
            for i in range(len(matrix[0])):
                matrix[x][i] = 0
        
