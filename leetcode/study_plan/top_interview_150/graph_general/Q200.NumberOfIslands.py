class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col, n, m):
            nonlocal grid
            if row < 0 or row >= n or col < 0 or col >= m:
                return

            if grid[row][col] == '0':
              return

            grid[row][col] = '0'

            dfs(row - 1, col, n , m)
            dfs(row + 1, col, n , m)
            dfs(row, col - 1, n , m)
            dfs(row, col + 1, n , m)

        n = len(grid)
        m = len(grid[0])
        count = 0

        for row in range(n):
            for col in range(m):
                if grid[row][col] != '0':
                    count += 1
                    dfs(row, col, n, m)
        return count
