class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            # New bit, def = 0
            ans = ans << 1
            # Bit val
            cur = n & 1
            # if 1 override
            ans = ans | cur
            # Next bit
            n = n >> 1
        return ans
