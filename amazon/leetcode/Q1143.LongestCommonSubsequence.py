class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1) + 1, len(text2) + 1
        dp = [[0 for _ in range(n)] for __ in range(m)]

        for j in range(1, m):
            for i in range(1, n):
                if text1[i - 1] == text2[j - 1]:
                    dp[j][i] = dp[j - 1][i - 1] + 1
                else:
                    dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])

        return dp[-1][-1]
