class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n

        if n == 1 or k == 0:
            return

        def reverse(start, end):
            while(start < end):
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Reverse array
        reverse(0, n - 1)
        # Reorder first k elements
        reverse(0, k - 1)
        # Reorder last n-k elements
        reverse(k, n - 1)
