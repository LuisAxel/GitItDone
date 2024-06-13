class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target:
            return 0

        ans = len(nums)
        prefix_sum = [0] * ans
        prefix_sum[0] = nums[0]

        for i,val in enumerate(nums[1:]):
            prefix_sum[i + 1] = prefix_sum[i] + val

        s = 0
        l = 0
        for r, val in enumerate(prefix_sum):
            s = val
            while s >= target:
                ans = min(ans, r - l + 1)
                s = val - prefix_sum[l]
                l += 1
        return ans
