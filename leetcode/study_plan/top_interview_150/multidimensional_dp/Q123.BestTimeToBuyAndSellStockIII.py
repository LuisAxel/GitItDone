class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n

        for _ in range(2):
            buy = -prices[0]
            profit = 0
            for i in range(1, n):
                # Keep bought stock or buy another one
                buy = max(buy, dp[i] - prices[i])
                # min profit = 0 (no transactions)
                profit = max(profit, buy + prices[i])
                dp[i] = profit

        return dp[-1]
