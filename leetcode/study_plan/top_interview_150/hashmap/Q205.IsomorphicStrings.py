class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        maped = set()

        for i, j in zip(s,t):
            # We have not maped char in s
            if i not in d:
                # We have already maped a char to this value
                if j in maped:
                    return False
                d[i] = j
                maped.add(j)
                continue

            if d[i] != j:
                return False
        return True
