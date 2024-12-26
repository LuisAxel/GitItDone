class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps = pt = 0
        ns, nt = len(s), len(t)

        while pt < nt:
            if ps == ns:
                break
            if s[ps] == t[pt]:
                ps += 1
            pt += 1

        return ps == ns
