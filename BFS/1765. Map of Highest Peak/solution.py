from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque()
        m = len(isWater)
        n = len(isWater[0])
        for row in range(m):
            for col in range(n):
                if isWater[row][col] == 1:
                    q.append((row, col))

        output = [[-1] * n for _ in range(m)]
        while q:
            row, col, h = q.popleft()
            output[row][col] = h
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row = row + x
                new_col = col + y
                if 0 <= new_row < m and 0 <= new_col < n and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    q.append((new_row, new_col, h + 1))

        return output
