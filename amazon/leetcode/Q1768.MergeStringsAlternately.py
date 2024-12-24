class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        ans = ''
        n1, n2 = len(word1), len(word2)

        i = 0
        while i < min(n1, n2):
            ans += word1[i] + word2[i]
            i += 1

        return ans + word1[i:] if n1 > n2 else ans + word2[i:]
