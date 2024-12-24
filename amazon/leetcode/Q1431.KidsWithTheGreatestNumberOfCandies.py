class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        target = max(candies)
        ans = [False] * len(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= target:
                ans[i] = True
        return ans
