class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) - 1
        l, r, found = 0, n, -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    found = mid
                    break
                else:
                    r = mid - 1
                    continue

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        if found == -1:
            return [-1, -1]

        l, r = found, n

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid == n or nums[mid + 1] != target:
                    break
                else:
                    l = mid + 1
                    continue

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return [found, mid]
