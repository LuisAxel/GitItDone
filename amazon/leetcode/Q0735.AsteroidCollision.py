class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []

        for ast in asteroids:
            cur = ast

            while ans and cur < 0 < ans[-1]:
                if -cur > ans[-1]:
                    ans.pop()
                    continue
                if -cur == ans[-1]:
                    ans.pop()
                cur = 0
                break

            if cur != 0:
                ans.append(cur)

        return ans
