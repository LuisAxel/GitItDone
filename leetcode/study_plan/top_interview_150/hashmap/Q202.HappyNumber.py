class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        s = n
        cur = 0

        while s != 1:
            cur = s
            s = 0
            while cur > 0:
                s += pow(cur % 10,2)
                cur = cur // 10
            if s in seen:
                return False
            seen.add(s)
        return True
