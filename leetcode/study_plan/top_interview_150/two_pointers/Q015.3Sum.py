class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        nums.sort()
        s = 0
        l, r = 0,0
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    ans.add((nums[i] ,nums[l] ,nums[r]))
                if s <= 0:
                    l += 1
                else:
                    r -= 1
        return ans
