class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r, mid = 0, len(nums) - 1, 0

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1
        return l
