class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        ans = 0
        l = r = 0
        count = 0

        while r < n:
            if nums[r] == 0:
                count += 1

            while count > 1:
                if nums[l] == 0:
                    count -=1
                l += 1

            r += 1
            ans = max(ans, r - l - count)

        return ans if ans < n else n - 1
