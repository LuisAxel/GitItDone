class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = ans = 0

        for netg in gain:
            cur += netg
            ans = max(ans, cur)

        return ans
