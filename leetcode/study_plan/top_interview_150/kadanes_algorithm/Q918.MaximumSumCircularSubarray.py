class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, cur_max, cur_min, max_found, min_found = 0, 0, 0, float('-inf'), float('inf')

        for num in nums:
            total += num
            cur_max = max(cur_max + num, num)
            cur_min = min(cur_min + num, num)
            max_found = max(max_found, cur_max)
            min_found = min(min_found, cur_min)

        return max_found if max_found < 0 else max(max_found, total - min_found)
