class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * (n)

        # Product left of this number
        prod = 1
        for i in range(0, n - 1):
            prod *= nums[i]
            answer[i + 1] = prod

        # Product right of this number
        prod = 1
        for i in range(n - 1, 0, -1):
            prod *= nums[i]
            answer[i - 1] *= prod

        return answer
