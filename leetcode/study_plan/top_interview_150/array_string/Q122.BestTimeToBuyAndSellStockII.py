class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for i in prices[1:]:
            # can make profit
            if i > buy:
                profit += i - buy
                buy = i
            # new lowest price
            else:
                buy = i

        return profit
