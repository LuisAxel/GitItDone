class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0
        l = 0
        r = len(height) - 1
        max_l, max_r = height[l], height[r]

        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(height[l], max_l)
                water += max_l - height[l]
            else:
                r -= 1
                max_r = max(height[r], max_r)
                water += max_r -height[r]

        return water
