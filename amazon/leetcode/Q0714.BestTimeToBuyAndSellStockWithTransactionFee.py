class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = prices[0] + fee
        profit = 0

        for price in prices[1:]:

            if price > buy:
                profit += price - buy
                buy = price
                continue

            buy = min(buy, price + fee)

        return profit
