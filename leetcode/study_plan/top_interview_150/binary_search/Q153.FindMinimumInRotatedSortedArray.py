class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums) - 1
        l, r = 0, n

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]

            # l-mid sorted
            if nums[l] <= nums[mid]:
                if nums[mid] < nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            # mid-r sorted
            else:
                if nums[mid] > nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
        return nums[mid]
