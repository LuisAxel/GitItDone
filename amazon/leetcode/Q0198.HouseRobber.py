class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        profit = [0] * n

        profit[0] = nums[0]
        profit[1] = max(nums[0], nums[1])

        for i in range(2, n):
            profit[i] = max(profit[i - 1], profit[i - 2] + nums[i])

        return profit[-1]
