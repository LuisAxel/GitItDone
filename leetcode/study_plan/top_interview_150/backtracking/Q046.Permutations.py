class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def helper(pool, cur):
            nonlocal ans

            # Permutations for 1 element = [element]
            if len(pool) == 1:
                ans.append(cur + [pool[0]])
                return

            for i in range(len(pool)):
                aux = pool.popleft()
                helper(pool, cur + [aux])
                pool.append(aux)

        p = deque(nums)
        ans = []
        helper(p, [])
        return ans
