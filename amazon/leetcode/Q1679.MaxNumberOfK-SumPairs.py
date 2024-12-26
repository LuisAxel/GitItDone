class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        l, r = 0, n - 1
        nums.sort()

        while l < r:
            cur = nums[l] + nums[r]
            if cur == k:
                ans += 1
                l += 1
                r -= 1
                continue

            if cur < k:
                l += 1
            else:
                r -= 1

        return ans
