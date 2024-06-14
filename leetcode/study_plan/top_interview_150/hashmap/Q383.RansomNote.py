class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n = len(ransomNote)
        r_d = defaultdict(int)

        for i in ransomNote:
            r_d[i] += 1

        count = 0

        for i in magazine:
            if r_d[i] > 0:
                count += 1
            r_d[i] -= 1
        return True if count == n else False
