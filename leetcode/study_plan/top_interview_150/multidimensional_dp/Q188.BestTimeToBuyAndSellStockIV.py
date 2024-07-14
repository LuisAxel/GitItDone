class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # if 2k >= n, return difference (unlimited transactions)
        if (k * 2) >= n:
            ans = 0
            for i in range(1, n):
                diff = prices[i] - prices[i - 1]
                ans += diff if diff > 0 else 0
            return ans

        dp = [0] * n
        for _ in range(k):
            buy = -prices[0]
            profit = 0
            for i in range(1, n):
                # Keep bought stock or buy another one
                buy = max(buy, dp[i] - prices[i])
                # min profit = 0 (no transactions)
                profit = max(profit, buy + prices[i])
                dp[i] = profit

        return dp[-1]
