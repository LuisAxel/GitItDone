class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        combined = []
        n = len(nums1)

        for i in range(n):
            combined.append([nums2[i], nums1[i]])

        combined.sort()
        heap = []
        ans = 0
        cur_sum = 0
        for mult, num in reversed(combined):
            heappush(heap, num)
            cur_sum += num

            if len(heap) == k:
                ans = max(ans, mult * cur_sum)
                cur_sum -= heappop(heap)

        return ans
