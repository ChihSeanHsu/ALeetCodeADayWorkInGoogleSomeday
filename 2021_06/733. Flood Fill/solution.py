class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        target = image[sr][sc]
        if newColor == target: 
            return image
        def dfs(row, col):
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != target:
                return 
        
            image[row][col] = newColor
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(row + x, col + y)
                
        dfs(sr, sc)
        return image
