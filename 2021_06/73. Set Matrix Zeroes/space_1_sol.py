class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    for i in range(len(matrix)):
                        if matrix[i][col] != 0:
                            matrix[i][col] = "a"
                            
                    for i in range(len(matrix[row])):
                        if matrix[row][i] != 0:
                            matrix[row][i] = "a"
                    
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == "a":
                    matrix[row][col] = 0
