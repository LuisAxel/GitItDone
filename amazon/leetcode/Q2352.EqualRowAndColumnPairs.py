class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = defaultdict(int)
        n = len(grid)

        ans = 0
        for row in grid:
            count[str(row)] += 1

        for i in range(n):
            col = []
            for j in range(n):
                col.append(grid[j][i])

            ans += count[str(col)]

        return ans
