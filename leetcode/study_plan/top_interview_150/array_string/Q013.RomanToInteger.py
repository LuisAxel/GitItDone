class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        ans = values[s[0]]

        for l,r in zip(s[:-1],s[1:]):
            ans += values[r]
            if l == 'I' and (r == 'V' or r == 'X'):
                ans -= 2
            elif l == 'X' and (r == 'L' or r == 'C'):
                ans -= 20
            elif l == 'C' and (r == 'D' or r == 'M'):
                ans -= 200
        return ans
