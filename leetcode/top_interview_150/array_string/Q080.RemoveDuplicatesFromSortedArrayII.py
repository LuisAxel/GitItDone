class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        write = 1
        i = 1
        twice = False

        # Bring to front uniques
        while i < n:
            if nums[i] == nums[write - 1]:
                if twice:
                    i += 1
                    continue
                else:
                    twice = True
            else:
                twice = False

            nums[write] = nums[i]
            write += 1
            i += 1

        return write
