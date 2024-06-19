class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def diff(a, b):
            count = 0
            for i in range(8):
                if a[i] != b[i]:
                    count += 1
            return count

        q = deque()
        seen = set()

        q.append([startGene, 0])

        while q:
            gene, mutations = q.popleft()

            if gene in seen:
                continue
            if gene == endGene:
                return mutations

            seen.add(gene)

            for test in bank:
                if test in seen:
                    continue
                if diff(gene, test) == 1:
                    q.append([test, mutations + 1])
        return -1
