class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 1
        points.sort(key=lambda x: x[1])

        arrow_shot = points[0][1]

        for start, end in points[1:]:
            if start <= arrow_shot:
                continue
            else:
                arrow_shot = end
                ans += 1

        return ans
