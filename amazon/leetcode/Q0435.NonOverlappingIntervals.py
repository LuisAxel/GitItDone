class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key=lambda x: x[1])

        prev_e = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_e:
                ans += 1
            else:
                prev_e = end

        return ans
