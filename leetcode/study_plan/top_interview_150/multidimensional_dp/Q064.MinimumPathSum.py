class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def getneigh(row, col, rows, cols):
            ans = []
            if row + 1 < rows:
                ans.append([row + 1, col])
            if col + 1 < cols:
                ans.append([row, col + 1])
            return ans

        def dfs(row, col, rows, cols, grid, cur):
            nonlocal distance
            cur += grid[row][col]
            if cur >= distance[row][col]:
                return

            distance[row][col] = cur
            neighs = getneigh(row, col, rows, cols)

            for neigh in neighs:
                dfs(neigh[0], neigh[1], rows, cols, grid, cur)

        rows = len(grid)
        cols = len(grid[0])
        distance = [[float('inf') for _ in range(cols)] for __ in range(rows)]
        dfs(0, 0, rows, cols, grid, 0)

        return distance[-1][-1]

