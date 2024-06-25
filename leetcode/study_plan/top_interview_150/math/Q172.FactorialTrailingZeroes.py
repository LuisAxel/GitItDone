class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0

        while n > 0:
            ans += n // 5
            n //= 5

        return ans
