class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs = sorted(strs)
        ans = ""

        for i in range(0,len(strs[0])):
            if strs[0][i] != strs[-1][i]:
                break
            ans += strs[0][i]
        return ans
