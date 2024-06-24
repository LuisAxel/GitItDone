class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        cur, n1, n2 = 0, len(nums1), len(nums2)
        heap = []
        heapify(heap)
        ans, visited = [], set()

        # smallest pair
        heappush(heap, (nums1[0] + nums2[0], (0, 0)))
        visited.add((0, 0))

        while cur < k and heap:
            idxs = heappop(heap)[1]
            ans.append([nums1[idxs[0]], nums2[idxs[1]]])

            if idxs[0] + 1 < n1 and (idxs[0] + 1, idxs[1]) not in visited:
                heappush(heap, (nums1[idxs[0] + 1] + nums2[idxs[1]], (idxs[0] + 1, idxs[1])))
                visited.add((idxs[0] + 1, idxs[1]))

            if idxs[1] + 1 < n2 and (idxs[0], idxs[1] + 1) not in visited:
                heappush(heap, (nums1[idxs[0]] + nums2[idxs[1] + 1], (idxs[0], idxs[1] + 1)))
                visited.add((idxs[0], idxs[1] + 1))

            cur += 1

        return ans
