# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        candidate = 0
        cur = root

        while cur:
            # Move to right child if left not found
            # Add 1 to current
            if cur.left is None:
                candidate += 1
                ans = max(ans, candidate)
                cur = cur.right

            # Find most right child of left
            else:
                left = 1
                prev = cur.left

                while prev.right and prev.right is not cur:
                    left += 1
                    prev = prev.right

                # current just moving to right
                # Add 1 to current
                if prev.right is None:
                    candidate += 1
                    prev.right = cur
                    cur = cur.left

                # returning from leaf to predecesor
                # substract [predecesor-leaf height] fom height
                else:
                    prev.right = None
                    cur = cur.right
                    ans = max(ans, candidate)
                    candidate -= left

        return ans
