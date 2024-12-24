class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = 1
        ans = [1] * n

        for i in range(0, n - 1):
            prod *= nums[i]
            ans[i + 1] *= prod

        prod = 1
        for i in range(n - 1, 0, -1):
            prod *= nums[i]
            ans[i - 1] *= prod

        return ans
