class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
        mid = n // 2

        # Let nums1 be the smaller array
        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1

        l, r = 0, n1 - 1

        while l <= n1:
            mid1 = (l + r) // 2
            mid2 = mid - mid1 - 2 # 0 indexed

            l1 = nums1[mid1] if mid1 >= 0 else float('-inf')
            l2 = nums2[mid2] if mid2 >= 0 else float('-inf')
            r1 = nums1[mid1 + 1] if mid1 + 1 < n1 else float('inf')
            r2 = nums2[mid2 + 1] if mid2 + 1 < n2 else float('inf')

            # Correct partition
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return min(r1, r2)
                else:
                    return (max(l1,l2) + min(r1, r2)) / 2

            # Increase or decrease partition size in small
            if l1 > r2:
                r = mid1 - 1
            else:
                l = mid1 + 1

        # Input wasn't sorted
        return -1
