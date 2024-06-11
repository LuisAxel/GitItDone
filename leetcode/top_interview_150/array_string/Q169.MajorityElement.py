class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0

        for i in nums:
            if count == 0:
                candidate = i
            count += 1 if candidate == i else -1

        return candidate
