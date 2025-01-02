# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root, left, size):
            if not root:
                self.ans = max(self.ans, size)
                return

            if left:
                dfs(root.left, False, size + 1)
                dfs(root.right, True, 0)
            else:
                dfs(root.right, True, size + 1)
                dfs(root.left, False, 0)

        dfs(root.right, True, 0)
        dfs(root.left, False, 0)

        return self.ans
