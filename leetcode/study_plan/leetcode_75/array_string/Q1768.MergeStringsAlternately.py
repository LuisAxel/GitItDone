class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)

        ans = ""
        i = 0
        while i < n1 and i < n2:
            ans += word1[i] + word2[i]
            i += 1
        ans += word2[i:] if n1 < n2 else word1[i:]

        return ans
