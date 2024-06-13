class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        l = 0

        for r,c in enumerate(s):
            if c not in seen:
                seen.add(c)
                max_len = max(max_len, r - l + 1)
            else:
                while s[l] != c:
                    seen.remove(s[l])
                    l += 1
                l += 1

        return max_len
