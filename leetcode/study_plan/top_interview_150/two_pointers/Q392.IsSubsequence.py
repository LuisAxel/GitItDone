class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, nl = 0, len(s)
        r, nr = 0, len(t)

        while l < nl and r < nr:
            if s[l] == t[r]:
                l +=1
                if l == nl:
                    return True
            r += 1
        return False if l != nl else True
