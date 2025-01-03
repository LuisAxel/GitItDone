class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def buildGraph(eq, values):
            graph = defaultdict(dict)

            for idx, vals in enumerate(eq):
                up, down = vals
                res = values[idx]

                graph[up][down] = res
                graph[down][up] = 1/res

            return graph

        def dfs(start, target, weight):
            nonlocal graph, visited, candidate
            if start in visited:
                return

            visited.add(start)

            if start == target:
                candidate = weight
                return

            for neigh in graph[start]:
                dfs(neigh, target, weight * graph[start][neigh])

        graph = buildGraph(equations, values)
        ans = []

        for q in queries:
            start, target = q
            if start not in graph or target not in graph:
                ans.append(-1.0)
                continue

            visited = set()
            candidate = -1.0
            weight = 1
            dfs(start, target, weight)
            ans.append(candidate)

        return ans
