class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for i in range(32):
            bit_count = 0
            for num in nums:
                if num < 0:
                    num &= 2**32 - 1
                bit_count += (num >> i) & 1
            if bit_count % 3 != 0:
                ans += 2**i

        if ans >= 2**31:
            ans -= 2**32

        return ans
