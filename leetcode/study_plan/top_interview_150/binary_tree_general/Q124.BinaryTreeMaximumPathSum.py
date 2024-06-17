# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = root.val

        def preorder(node):
            nonlocal max_path_sum

            # empty path sum -> 0
            if not node:
                return 0

            l_max = max(0, preorder(node.left))
            r_max = max(0, preorder(node.right))

            max_path_sum = max(max_path_sum, l_max + r_max + node.val)

            return node.val + max(l_max, r_max)

        preorder(root)
        return max_path_sum
