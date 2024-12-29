class Solution:
    def removeStars(self, s: str) -> str:
        ans = ""
        stars = 0
        i = len(s) - 1

        while i >= 0:
            if s[i] == '*':
                stars += 1
                i -= 1
                continue
            if stars == 0:
                ans += s[i]
            else:
                stars -= 1
            i -= 1

        return ans[::-1]
