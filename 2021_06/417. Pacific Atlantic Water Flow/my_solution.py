class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def is_pacific(row, col):
            return True if col < 0 or row < 0 else False
        
        def is_atlantic(row, col):
            return True if row >= len(heights) or col >= len(heights[0]) else False

        def helper(row, col, visited, to_oceans):
            visited.add((row, col))

            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + x, col + y 
                if not (new_row, new_col) in visited:
                    pacific = is_pacific(new_row, new_col)
                    atlantic = is_atlantic(new_row, new_col)
                    if pacific:
                        to_oceans[0] = True
                    elif atlantic:
                        to_oceans[1] = True
                    elif not (pacific and atlantic) and heights[row][col] >= heights[new_row][new_col]:
                        helper(new_row, new_col, visited, to_oceans)
        
        result = []
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                visited = set()
                # to_pacific, to_atlantic
                to_oceans = [False, False]
                helper(r, c, visited, to_oceans)
                if all(to_oceans):
                    result.append((r, c))
        
        return result
