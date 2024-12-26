class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        ans = 0
        n = len(nums)
        zeroes = 0

        while r < n:
            # Increase window
            if nums[r] == 0:
                zeroes += 1
            r += 1

            # Shrink window if needed
            while zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1

            ans = max(ans, r - l)

        return ans
