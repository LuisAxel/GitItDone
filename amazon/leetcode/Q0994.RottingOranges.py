class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        fresh = 0
        q = deque()

        for y in range(n):
            for x in range(m):
                if grid[y][x] == 2:
                    q.append([y, x])
                elif grid[y][x] == 1:
                    fresh += 1

        time = 0
        while q and fresh > 0:
            time += 1
            rottens = len(q)
            for rotten in range(rottens):
                y, x = q.popleft()

                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ny = y + dy
                    nx = x + dx
                    if (0 <= nx < m and 0 <= ny < n) and grid[ny][nx] == 1:
                        q.append([ny, nx])
                        grid[ny][nx] = 2
                        fresh -= 1

        return time if fresh <= 0 else -1
