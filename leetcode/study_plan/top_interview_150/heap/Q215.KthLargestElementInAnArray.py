class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # We only want to store at most k elements
        heap = nums[:k]
        heapify(heap)

        # We already saved first k elements in the heap
        for num in nums[k:]:
            # current is bigger than smallest big element
            if num > heap[0]:
                heappushpop(heap, num)

        return heap[0]
