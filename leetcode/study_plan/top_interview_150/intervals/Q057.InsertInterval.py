class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        intervals.append(newInterval)
        intervals.reverse()

        for i, v in enumerate(intervals[1:]):
            if v[0] > newInterval[0]:
                intervals[i] = v
                continue
            intervals[i] = newInterval
            break

        # newInterval is the smallest
        if intervals[-1] == intervals[-2]:
            intervals[-1] = newInterval

        intervals.reverse()
        ans = [intervals[0]]

        for s, e in intervals[1:]:
            if s > ans[-1][1]:
                ans.append([s, e])
                continue
            ans[-1][1] = max(ans[-1][1], e)
        return ans
