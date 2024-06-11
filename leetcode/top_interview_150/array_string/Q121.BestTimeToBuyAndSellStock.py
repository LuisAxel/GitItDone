class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        best_buy = prices[0]

        for i in prices[1:]:
            # can make profit
            if i > best_buy:
                profit = max(profit, i - best_buy)
            # new lowest price
            else:
                best_buy = i

        return profit
