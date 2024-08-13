class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        ans = 0
        for num in nums:
            times = 1 if k - num == num else 0
            if count[k - num] > 0 and count[num] > times:
                ans += 1
                count[k - num] -= 1
                count[num] -= 1

        return ans
