# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root

        while cur:
            # Go to rightmost leaf of left
            if cur.left:
                prev = cur.left
                while prev.right:
                    prev = prev.right
                # Assign right sub tree to right's rightmost leaf of left
                prev.right = cur.right
                # Move left sub tree to its right
                cur.right = cur.left
                # Remove left
                cur.left = None
            # Move to next node
            cur = cur.right
