class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        len_LIS = [1] * n

        for ends in range(n):
            for cur in range(ends):
                if nums[ends] > nums[cur]:
                    len_LIS[ends] = max(len_LIS[ends], len_LIS[cur] + 1)
        return max(len_LIS)
