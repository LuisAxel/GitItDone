class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)

        if ns != nt:
            return False

        ds = defaultdict(int)
        for i in s:
            ds[i] += 1

        for j in t:
            if ds[j] <= 0:
                return False
            ds[j] -= 1
        return True
