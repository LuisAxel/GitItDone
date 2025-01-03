class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighs = defaultdict(list)

        for a, b in connections:
            neighs[a].append([b, True])
            neighs[b].append([a, False])

        ans = 0
        q = []
        q.append(0)
        visited = set()

        while q:
            cur = q.pop()
            visited.add(cur)
            for neigh, direction in neighs[cur]:
                if neigh not in visited:
                    q.append(neigh)
                    ans += direction
        return ans
