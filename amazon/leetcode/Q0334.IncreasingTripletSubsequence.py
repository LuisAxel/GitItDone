class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = j = float('inf')

        for num in nums:
            if num <= i:
                i = num
                continue
            if num <= j:
                j = num
                continue
            return True
        return False
