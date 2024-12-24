class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a','e','i','o','u'])
        ans = list(s)

        l, r = 0, len(s) - 1
        while l < r:

            while ans[l].lower() not in vowels and l < r:
                l += 1
            while ans[r].lower() not in vowels and l < r:
                r -= 1

            if l < r:
                ans[l], ans[r] = ans[r], ans[l]
                l += 1
                r -= 1

        return "".join(ans)
