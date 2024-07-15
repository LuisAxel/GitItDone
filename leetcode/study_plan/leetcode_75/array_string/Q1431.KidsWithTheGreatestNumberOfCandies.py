class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatestCandies = max(candies)
        ans = [False] * len(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatestCandies:
                ans[i] = True
        return ans
