class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(s):
            return s[::-1]

        # Reverse whole string and remove spaces
        s = reverse(" ".join(s.split()))
        n = len(s)
        start = 0
        idx = 0

        while idx < n:
            if s[idx] == ' ':
                idx += 1

            start = idx
            # Reverse reversed words
            while idx < n and s[idx] != ' ':
                idx += 1
            s = s[:start] + reverse(s[start:idx]) + s[idx:]

        return s
