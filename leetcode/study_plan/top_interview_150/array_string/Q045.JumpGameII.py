class Solution:
    def jump(self, nums: List[int]) -> int:

        pos = 0
        jumps = 0
        far = nums[0]
        n = len(nums) - 1

        while far < n:
            far = nums[pos] + pos
            #Check for new farthest location
            for i in range(pos + 1, far + 1):
                if nums[i] + i > far:
                    far = nums[i] + i
                    pos = i
            jumps += 1

        #Check if we jumped to the location
        return jumps + 1 if pos < n else jumps
