class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a > 0 or b > 0 or c > 0:
            ba = a & 1
            bb = b & 1
            bc = c & 1

            if not bc:
                ans += ba + bb
            elif not ba and not bb:
                ans += 1

            a = a // 2
            b = b // 2
            c = c // 2

        return ans
