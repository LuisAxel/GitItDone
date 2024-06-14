class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ls = s.split()
        if len(pattern) != len(ls):
            return False

        d = {}
        maped = set()
        for i,val in enumerate(ls):
            if val not in d:
                if pattern[i] in maped:
                    return False
                d[val] = pattern[i]
                maped.add(pattern[i])
                continue

            if d[val] != pattern[i]:
                return False
        return True
