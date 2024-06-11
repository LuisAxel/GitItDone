class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        write = 0

        # Bring elements != val to front
        while i < n:
            if nums[i] == val:
                i += 1
                continue
            nums[write] = nums[i]
            write += 1
            i += 1

        # Remove val spaces
        while write < i:
            nums.pop()
            write += 1
