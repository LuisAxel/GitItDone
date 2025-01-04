class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for __ in range(m)]

        for i in range(n):
            dp[0][i] = 1

        for i in range(m):
            dp[i][0] = 1

        for j in range(1, m):
            for i in range(1, n):
                dp[j][i] = dp[j - 1][i] + dp[j][i - 1]

        return dp[-1][-1]
