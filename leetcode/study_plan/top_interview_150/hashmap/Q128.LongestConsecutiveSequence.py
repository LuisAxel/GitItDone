class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        cur = 0
        i = 0

        for num in num_set:
            i = num
            # Only count for start of sequence
            if i - 1 not in num_set:
                cur = 0
                while i in num_set:
                    cur += 1
                    i += 1
                if cur > ans:
                    ans = cur
        return ans
