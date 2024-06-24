class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        heapify(heap)

        n = len(profits)
        projects = [[capital[project], profits[project]] for project in range(n)]
        projects.sort()

        project = 0
        for action in range(k):
            # While projects and affordable
            while project < n and projects[project][0] <= w:
                # python heap = min_heap so -
                heappush(heap, -projects[project][1])
                project += 1

            # capitals are not substracted, just add profit
            w -= heappop(heap) if heap else 0
        return w
