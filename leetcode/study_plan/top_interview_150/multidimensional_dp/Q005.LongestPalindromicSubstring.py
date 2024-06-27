class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def helper(left, right, s, n):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        ans = s[0]
        for i in range(1, n):
            one = helper(i, i, s, n)
            two = helper(i - 1, i, s, n)

            if len(ans) < len(one):
                ans = one
            if len(ans) < len(two):
                ans = two

        return ans
