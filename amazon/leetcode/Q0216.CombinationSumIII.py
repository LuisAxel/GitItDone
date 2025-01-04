class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(start, cur, l, total):
            if l == k:
                if total == n:
                    ans.append(cur)
                return

            for i in range(start, 10):
                cur_total = total + i
                if cur_total > n:
                    return
                dfs(i + 1, cur + [i], l + 1, cur_total)

        ans = []
        dfs(1,[], 0, 0)
        return ans
