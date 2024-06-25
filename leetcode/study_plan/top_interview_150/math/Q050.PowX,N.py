class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x

        ans = 1
        while n > 0:
            # x^n = (x^(n/2))^2
            if n % 2 == 0:
                x *= x
                n //= 2
            else:
                ans *= x
                n -= 1

        return ans
