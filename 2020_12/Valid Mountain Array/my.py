class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        up = False
        down = False
        cursor = None
        for i in arr:
            if cursor is None:
                cursor = i
                continue
            if up and down and i > cursor:
                up = down = False
                break
            if i > cursor:
                cursor = i
                up = True
            elif i == cursor:
                up = down = False
                break
            elif i < cursor and up:
                cursor = i
                down = True
        return up and down
            
        
