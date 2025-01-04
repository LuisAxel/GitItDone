class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        def dfs(i, cur, digits):
            if len(cur) == len(digits):
                ans.append(cur)
                return

            for letter in letters[digits[i]]:
                dfs(i + 1, cur + letter, digits)

        letters = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs",
                "8" : "tuv", "9" : "wxyz"}
        ans = []
        dfs(0, "", digits)
        return ans
