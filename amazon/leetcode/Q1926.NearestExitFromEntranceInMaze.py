class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ans = -1
        n = len(maze)
        m = len(maze[0])
        q = deque()
        q.append([entrance, 0])

        maze[entrance[0]][entrance[1]] = "+"

        while q:
            pos, steps = q.popleft()
            y, x = pos
            maze[y][x] = '+'

            if ((y == 0 or y == n - 1) or (x == 0 or x == m - 1)) and [y,x] != entrance:
                ans = steps
                break

            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[ny][nx] == '.':
                    maze[ny][nx] = '+'
                    q.append([[ny, nx], steps + 1])


        return ans
