class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for _ in range(cols)] for __ in range(rows)]
        ans = 0

        for row in range(rows):
            dp[row][0] = int(matrix[row][0])
            ans = max(ans, dp[row][0])

        for col in range(cols):
            dp[0][col] = int(matrix[0][col])
            ans = max(ans, dp[0][col])

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == '0':
                    continue
                dp[row][col] = 1 + min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1])
                ans = max(ans, dp[row][col])

        return ans*ans
