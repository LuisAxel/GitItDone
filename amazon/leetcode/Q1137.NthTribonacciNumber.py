class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0
        if n < 3:
            return 1

        a, b, c = 0, 1, 1

        for i in range(n - 2):
            a += b + c
            a, b, c = b, c, a

        return c
