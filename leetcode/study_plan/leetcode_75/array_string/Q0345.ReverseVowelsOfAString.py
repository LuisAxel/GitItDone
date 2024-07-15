class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"A","E","I","O","U","a","e","i","o","u"}
        ans = list(s)

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] not in vowels:
                i += 1
                continue
            if s[j] not in vowels:
                j -= 1
                continue

            ans[i], ans[j] = ans[j], ans[i]
            i += 1
            j -= 1

        return "".join(ans)
