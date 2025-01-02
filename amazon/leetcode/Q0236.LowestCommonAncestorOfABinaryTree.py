# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(root):
            # Base case
            if not root:
                return

            # Found P or Q
            if root == p or root == q:
                return root

            # Search for P and Q
            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                return root

            return left or right

        return dfs(root)
