class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        ans, cur = float('-inf'), 0
        for num in nums:
            # current sequence or new sequence
            cur = max(cur + num, num)
            ans = max(ans, cur)
        return ans
