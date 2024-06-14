class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        shot = points[0][1]
        ans = 1

        for s, e in points[1:]:
            if s > shot:
                ans += 1
                shot = e
            shot = min(shot, e)

        return ans
