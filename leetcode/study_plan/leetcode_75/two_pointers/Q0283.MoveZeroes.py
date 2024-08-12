class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, n = 0, len(nums)
        for r in range(l, n):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
