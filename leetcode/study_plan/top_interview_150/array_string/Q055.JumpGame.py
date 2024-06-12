class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        # no jumps available and are required
        if n > 1 and nums[0] == 0:
            return False

        jump = nums[0]
        last = 0
        idx = 1

        while idx < n:

            # out of jumps
            if jump - (idx - last) <= 0:
                if idx != n - 1 and nums[idx] == 0:
                    return False
            # jump for more steps
            if jump - (idx - last) < nums[idx]:
                last = idx
                jump = nums[idx]
            idx += 1

        return True
