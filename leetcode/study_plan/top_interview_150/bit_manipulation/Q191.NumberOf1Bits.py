class Solution:
    def hammingWeight(self, n: int) -> int:
        div = 2**30
        ans = 0

        while div > 0:
            if div <= n:
                n -= div
                ans += 1
            div = div >> 1
        return ans
