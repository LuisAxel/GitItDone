class Solution:
    def numTilings(self, n: int) -> int:
        full = defaultdict(int)
        tromino = defaultdict(int)

        full[0] = 1
        full[1] = 1

        for i in range(2, n + 1):
            full[i] = full[i - 1] + full[i - 2] + (2 * tromino[i - 1])
            tromino[i] = full[i - 2] + tromino[i - 1]

        return full[n] % (10 ** 9 + 7)
