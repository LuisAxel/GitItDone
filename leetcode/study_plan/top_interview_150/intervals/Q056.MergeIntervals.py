class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        ans = [intervals[0]]

        for s, e in intervals[1:]:
            if s > ans[-1][1]:
                ans.append([s, e])
                continue
            ans[-1][1] = max(ans[-1][1], e)

        return ans
