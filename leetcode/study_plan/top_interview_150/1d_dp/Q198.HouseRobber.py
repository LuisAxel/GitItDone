class Solution:
    def rob(self, nums: List[int]) -> int:
        profit = nums
        for i in range(2, len(nums)):
            if i - 3 >= 0:
                profit[i] += max(profit[i - 2], profit[i - 3])
            else:
                profit[i] += profit[i - 2]

        return max(profit)
