class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node, visited, isConnected):
            visited.add(node)

            for idx, val in enumerate(isConnected[node]):
                if val == 0 or idx in visited:
                    continue
                if val == 1:
                    dfs(idx, visited, isConnected)

        ans = 0
        visited = set()

        for i in range(len(isConnected)):
            if i not in visited:
                ans += 1
                dfs(i, visited, isConnected)
        return ans
