class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        write = 1
        i = 1

        # Bring to front uniques
        while i < n:
            if nums[i] == nums[write - 1]:
                i += 1
                continue

            nums[write] = nums[i]
            write += 1
            i += 1

        # Remove duplicate spaces
        while write < i:
            nums.pop()
            write += 1
