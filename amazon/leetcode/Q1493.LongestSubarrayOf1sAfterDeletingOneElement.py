class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        count = 0
        n = len(nums)
        ans = 0

        while r < n:
            if nums[r] == 0:
                count += 1
            r += 1

            while count > 1:
                if nums[l] == 0:
                    count -= 1
                l += 1

            ans = max(ans, r - l - 1) # must delete an element

        return ans
