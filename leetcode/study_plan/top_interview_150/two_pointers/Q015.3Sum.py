class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k]  == 0:
                        if (nums[i],nums[j],nums[k]) not in ans:
                            ans.add((nums[i] ,nums[j] ,nums[k]))
        return ans
