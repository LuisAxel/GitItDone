class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1

        for i in range(1, n):
            b = b + a
            a = b - a
        return b
