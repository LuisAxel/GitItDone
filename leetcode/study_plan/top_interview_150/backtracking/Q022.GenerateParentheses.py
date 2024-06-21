class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(cur, left, right, n):
            nonlocal ans
            if len(cur) ==  n * 2:
                ans.append(cur)
                return

            if left < n:
                helper(cur + '(', left + 1, right, n)

            if left > right:
                helper(cur + ')', left, right + 1, n)

        ans = []
        helper("", 0, 0, n)
        return ans
