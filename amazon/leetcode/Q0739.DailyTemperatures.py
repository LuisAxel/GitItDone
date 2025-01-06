class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        pending = []

        for i in range(n):
            while pending and temperatures[i] > temperatures[pending[-1]]:
                idx = pending.pop()
                ans[idx] = i - idx
            pending.append(i)

        return ans
