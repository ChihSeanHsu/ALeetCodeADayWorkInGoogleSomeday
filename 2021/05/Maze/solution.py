from collections import defaultdict

class Solution:

    def sol(self, maze: list(list), start: list, destination: list) -> (bool):
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = [[False for _ in range(len(maze)) ] for _ in range(len(maze[0]))]
        stack = []
        visit[start[0]][start[1]] = True
        stack.append(start)
        while stack:
            p = stack.pop()
            if p[0] == destination[0] and p[1] == destination[1]:
                return True
            
            for d in dirs:
                x = p[0] + d[0]
                y = p[1] + d[1]

                while x >= 0 and y >= 0 and x < len(maze) and y < len(maze[0]) and maze[x][y] == 0:
                    x += d[0]
                    y += d[1]

                corrected_pos = [x - d[0], y - d[1]]
                if not visit[corrected_pos[0]][corrected_pos[1]]:
                    stack.append(correct_pos)
                    visit[corrected_pos[0]][corrected_pos[1]] = True

        return False

