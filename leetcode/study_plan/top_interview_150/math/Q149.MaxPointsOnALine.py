class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 1
        for i, point1 in enumerate(points):
            slopes = defaultdict(int)
            for j, point2 in enumerate(points[i + 1:]):
                if point1[0] == point2[0]:
                    slope = float('inf')
                else:
                    slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
                slopes[slope] += 1
                ans = max(ans, slopes[slope] + 1)

        return ans
