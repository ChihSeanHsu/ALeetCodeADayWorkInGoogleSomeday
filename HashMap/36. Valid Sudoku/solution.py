from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(row, col):
            for i in range(9):
                if i == col or board[row][i] == ".":
                    continue
                if board[row][i] == board[row][col]:
                    return False
                
            return True
        
        def check_col(row, col):
            for i in range(9):
                if i == row or board[i][col] == ".":
                    continue
                if board[i][col] == board[row][col]:
                    return False
                
            return True
        
        def check_block(row, col):
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3

            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if (i == row and j == col) or board[i][j] == ".":
                        continue
                    if board[i][j] == board[row][col]:
                        return False
            
            return True

        result = True
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                result = all([result, check_row(row, col), check_col(row, col), check_block(row, col)])
                
        return result
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_mapping = defaultdict(set)
        row_mapping = defaultdict(set)
        block_mapping = defaultdict(set)

        for row in range(9):
            for col in range(9):
                block = f"{(row // 3) * 3}_{(col // 3) * 3}"
                value = board[row][col]
                if board[row][col] == ".":
                    continue
                if value in col_mapping[col]:
                    return False
                if value in row_mapping[row]:
                    return False
                if value in block_mapping[block]:
                    return False
                
                col_mapping[col].add(value)
                row_mapping[row].add(value)
                block_mapping[block].add(value)
   
        return True
