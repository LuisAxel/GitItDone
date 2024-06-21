class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(first, cur, s):
            nonlocal ans, candidates, n, target

            if s == target:
                ans.append(cur)
                return
            if s > target:
                return

            for i in range(first, n):
                helper(i, cur + [candidates[i]], s + candidates[i])

        ans = []
        n = len(candidates)
        helper(0, [], 0)
        return ans
