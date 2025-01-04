class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(piles, k, h):

            ans = 0
            for pile in piles:
                ans += math.ceil(pile / k)

            return ans <= h

        l, r = 1, max(piles)

        while l <= r:
            m = (l + r) // 2
            if canEat(piles, m, h):
                r = m - 1
            else:
                l = m + 1

        return l
