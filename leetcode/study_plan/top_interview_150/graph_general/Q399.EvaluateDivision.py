class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def buildGraph(eq, values):
            graph = {}

            for i, v in enumerate(eq):
                up, down = v
                res = values[i]

                if up not in graph:
                    graph[up] = {}
                if down not in graph:
                    graph[down] = {}

                graph[up][down] = res
                graph[down][up] = 1/res

            return graph

        def dfs(up, down, cur):
            nonlocal graph, visited, candidate
            if up in visited:
                return

            visited.add(up)

            if up == down:
                candidate = cur
                return

            for neigh in graph[up]:
                dfs(neigh, down, cur * graph[up][neigh])

        graph = buildGraph(equations, values)
        ans = []

        for q in queries:
            up, down = q
            if up not in graph or down not in graph:
                ans.append(-1.0)
                continue

            visited = set()
            candidate = -1.0
            cur = 1
            dfs(up, down, cur)
            ans.append(candidate)

        return ans
