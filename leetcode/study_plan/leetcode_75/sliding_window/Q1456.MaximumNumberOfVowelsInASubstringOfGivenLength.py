class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        ans = 0

        for i in range(0, k):
            ans += 1 if s[i] in vowels else 0

        cur = ans
        for i in range(k, len(s)):
            cur += 1 if s[i] in vowels else 0
            cur -= 1 if s[i - k] in vowels else 0
            ans = max(ans, cur)

        return ans
