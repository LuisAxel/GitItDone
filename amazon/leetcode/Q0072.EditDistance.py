class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1) + 1, len(word2) + 1
        dp = [[float('inf') for _ in range(n)]for __ in range(m)]

        for i in range(n):
            dp[0][i] = i

        for i in range(m):
            dp[i][0] = i

        for j in range(1, m):
            for i in range(1, n):
                if word1[i - 1] == word2[j - 1]:
                    dp[j][i] = dp[j - 1][i - 1]
                else:
                    dp[j][i] = min(dp[j - 1][i - 1], dp[j - 1][i], dp[j][i - 1]) + 1

        return dp[-1][-1]
