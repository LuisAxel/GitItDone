class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r, n = 0, k, len(nums)
        cur = ans = sum(nums[l:r])

        while r < n:
            cur += nums[r] - nums[l]
            r += 1
            l += 1
            ans = max(ans, cur)

        return ans / k
