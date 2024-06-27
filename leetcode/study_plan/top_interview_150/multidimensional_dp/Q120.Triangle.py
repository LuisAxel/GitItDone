class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = triangle[-1]
        rows = len(triangle) - 1

        for row in range(rows - 1, -1, -1):
            for cur in range(row + 1):
                memo[cur] = min(triangle[row][cur] + memo[cur], triangle[row][cur] + memo[cur + 1])
        return memo[0]
