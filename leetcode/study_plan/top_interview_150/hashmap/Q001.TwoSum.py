class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        c = defaultdict(int)

        for i,v in enumerate(nums):
            d[v] = i
            c[v] += 1

        for i,v in enumerate(nums):
            if target - v in nums:
                if target - v == v and c[v] < 2:
                    continue
                return [i, d[target - v]]

        return [-1,-1]
