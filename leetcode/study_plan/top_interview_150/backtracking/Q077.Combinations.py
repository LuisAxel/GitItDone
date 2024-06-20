class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(f, cur, cur_l):
            nonlocal ans, n

            if cur_l == k:
                ans.append(cur)
                return

            for i in range(f, n + 1):
                backtrack(i + 1, cur + [i], cur_l + 1)

        ans = []
        backtrack(1, [], 0)
        return ans
