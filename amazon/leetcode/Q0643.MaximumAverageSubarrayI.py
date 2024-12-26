class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = cur = sum(nums[:k])
        n = len(nums)
        r = k

        while r < n:
            cur += nums[r] - nums[r - k]
            ans = max(ans, cur)
            r += 1

        return ans / k
