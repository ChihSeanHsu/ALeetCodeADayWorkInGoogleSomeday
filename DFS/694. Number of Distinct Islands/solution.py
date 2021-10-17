class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        """

        [
            [1,1,0,1,1],
            [1,0,0,0,0],
            [0,0,0,0,1],
            [1,1,0,1,1]
        ]

        ((0,0), (0,1), (1,0)) 
        ((0,3), (0,4)) -> ((0, 0), (0, 1))
        ((3,0), (3,1)) -> ((0, 0), (0, 1))
        ((2, 3), (3, 2), (3, 3)) -> ((0, 0), (1, -1), (1, 0))

        """

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(base_row, base_col, i, j, shape):
            rows = len(grid)
            cols = len(grid[0])
            if i < 0 or i > rows - 1 or j < 0 or j > cols - 1 or grid[i][j] != 1:
                return 

            grid[i][j] = -1
            shape.append((i - base_row, j - base_col))

            for new_i, new_j in dirs:
                dfs(base_row, base_col, i + new_i, j + new_j, shape)

        distinct_islands = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 1:
                    continue
                    
                shape = []
                dfs(row, col, row, col, shape)
                
                distinct_islands.add(tuple(shape))

        return len(distinct_islands)
        
