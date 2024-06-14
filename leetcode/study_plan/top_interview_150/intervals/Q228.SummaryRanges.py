class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [str(nums[0])]

        l = nums[0]
        cur = nums[0]
        ans = []

        for num in nums[1:]:
            if num == cur + 1:
                cur = num
                continue
            if l != cur:
                ans.append(str(l) + '->' + str(cur))
            else:
                ans.append(str(l))
            cur = num
            l = cur

        if l != cur:
            ans.append(str(l) + '->' + str(cur))
        else:
            ans.append(str(l))

        return ans
