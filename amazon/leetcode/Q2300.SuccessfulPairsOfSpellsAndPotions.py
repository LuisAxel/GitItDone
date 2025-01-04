class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def bs(potions, val, success):
            l, r = 0, len(potions) - 1
            min_idx = float('inf')
            while l <= r:
                m = (l + r) // 2
                if potions[m] * val >= success:
                    min_idx = min(min_idx, m)
                    r = m - 1
                else:
                    l = m + 1
            return len(potions) - min_idx

        potions.sort()
        ans = []
        for spell in spells:
            if spell * potions[-1] < success:
                ans.append(0)
                continue
            else:
                ans.append(bs(potions, spell, success))

        return ans
