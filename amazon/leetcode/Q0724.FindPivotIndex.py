class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum, rsum = 0, sum(nums)

        for idx, val in enumerate(nums):
            if lsum == rsum - val:
                return idx
            lsum += val
            rsum -= val

        return -1
