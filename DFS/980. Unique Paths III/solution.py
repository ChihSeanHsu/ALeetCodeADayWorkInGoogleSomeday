class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def helper(row, col, zeros, seen):
            if grid[row][col] == 2:
                if zeros == 0:
                    self.result += 1
                return
                
            seen.add((row, col))
            if grid[row][col] == 0:
                zeros -= 1
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_x = row + x
                new_y = col + y
                if (new_x, new_y) not in seen and 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] != -1:
                    helper(new_x, new_y, zeros, seen)
            seen.remove((row, col))
        
        self.result = 0
        cols = len(grid[0])
        rows = len(grid)
        
        zeros = 0
        start_point = None
        for row in range(rows):
            for col in range(cols):
                curr = grid[row][col]
                if curr == 0:
                    zeros += 1
                
                if curr == 1:
                    start_point = (row, col)
                    
        helper(start_point[0], start_point[1], zeros, set())
        
        return self.result
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def helper(row, col, zeros):
            if 0 > row or row >= rows or 0 > col or col >= cols or grid[row][col] < 0:
                return
                    
            if grid[row][col] == 2:
                if zeros == 0:
                    self.result += 1
                return
                
            if grid[row][col] == 0:
                zeros -= 1
            save = grid[row][col]
            grid[row][col] = -2
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_x = row + x
                new_y = col + y
                helper(new_x, new_y, zeros)
            grid[row][col] = save
        
        self.result = 0
        cols = len(grid[0])
        rows = len(grid)
        
        zeros = 0
        start_point = None
        for row in range(rows):
            for col in range(cols):
                curr = grid[row][col]
                if curr == 0:
                    zeros += 1
                
                if curr == 1:
                    start_point = (row, col)
                    
        helper(start_point[0], start_point[1], zeros)
        
        return self.result
                    
        
