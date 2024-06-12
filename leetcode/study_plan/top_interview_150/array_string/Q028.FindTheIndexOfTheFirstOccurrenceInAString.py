class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n = len(haystack)
        n2 = len(needle)
        i, j = 0, 0
        last = 0

        while i < n:
            j = 0
            last = i
            while i < n and j < n2 and needle[j] == haystack[i]:
                i += 1
                j += 1
            if j == n2:
                break
            i = last
            i += 1

        return i - j if j == n2 else -1
