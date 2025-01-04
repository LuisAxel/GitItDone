class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heapleft = []
        heapright = []
        i, j = 0, len(costs) - 1
        cost = 0

        while k > 0:
            k -= 1
            while len(heapleft) < candidates and i <= j:
                heappush(heapleft, costs[i])
                i += 1

            while len(heapright) < candidates and i <= j:
                heappush(heapright, costs[j])
                j -= 1

            left = heapleft[0] if heapleft else float('inf') 
            right = heapright[0] if heapright else float('inf')

            if left <= right:
                cost += heappop(heapleft)
            else:
                cost += heappop(heapright)
        return cost
