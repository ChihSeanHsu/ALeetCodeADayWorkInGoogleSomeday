class Solution:
  
    # from center
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check_flip(row, col, store_grid) -> bool:
            if row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1:
                return False

            need_flip = True
            seen.add((row, col))
            store_grid.append((row, col))
            for x, y in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                new_x = row + x
                new_y = col + y
                if board[new_x][new_y] == "O" and (new_x, new_y) not in seen:
                    need_flip = all([check_flip(new_x, new_y, store_grid), need_flip])

            return need_flip      

        seen = set()
        for row in range(1, len(board) - 1):
            for col in range(1, len(board[0]) - 1):
                if board[row][col] == "O" and (row, col) not in seen:
                    store_grid = []
                    need_flip = check_flip(row, col, store_grid)
                    if need_flip:
                        for x, y in store_grid:
                            board[x][y] = "X"

    # for border
    def solve(self, board: List[List[str]]) -> None:
        col_len = len(board[0])
        row_len = len(board)
        def dfs(row, col):
            board[row][col] = "S"
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_x = row + x
                new_y = col + y
                if 0 <= new_x < row_len and 0 <= new_y < col_len and board[new_x][new_y] == "O":
                    dfs(new_x, new_y)
        
        for row in (0, row_len - 1):
            for col in range(col_len):
                if board[row][col] == "O":
                    dfs(row, col)
                    
        for row in range(row_len):
            for col in (0, col_len - 1):
                if board[row][col] == "O":
                    dfs(row, col)
        
        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "S":
                    board[row][col] = "O"
            
        
        
