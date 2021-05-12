class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.each_field_sum_up = []
        prev_row_sum = [0] * len(matrix[0])
        for idx, row in enumerate(matrix):
            total = 0
            curr = []
            for i, v in enumerate(row):
                total += v
                curr.append(total + prev_row_sum[i])
            self.each_field_sum_up.append(curr)
            prev_row_sum = curr
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1:
            top = self.each_field_sum_up[row1 - 1][col2]
        else:
            top = 0
        
        if col1:
            left = self.each_field_sum_up[row2][col1 - 1]
        else:
            left = 0
            
        if col1 and row1:
            top_left = self.each_field_sum_up[row1 - 1][col1 - 1]
        else:
            top_left = 0
            
        return self.each_field_sum_up[row2][col2] - top - left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
