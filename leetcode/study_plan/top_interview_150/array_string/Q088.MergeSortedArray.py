class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1

        for _ in range(m + n - 1, -1, -1):
            # Nothing to sort
            if j < 0:
                break
            # Copy rest of 2
            elif i < 0:
                nums1[_] = nums2[j]
                j -= 1
            # Merge
            else:
                if (nums1[i] > nums2[j]):
                    nums1[_] = nums1[i]
                    i -= 1
                else:
                    nums1[_] = nums2[j]
                    j -= 1
