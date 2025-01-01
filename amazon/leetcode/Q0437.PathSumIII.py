# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.lookup = defaultdict(int)
        self.lookup[targetSum] = 1
        self.ans = 0

        def dfs(root, root_sum):
            if not root:
                return

            root_sum += root.val
            self.ans += self.lookup[root_sum]

            self.lookup[root_sum + targetSum] += 1
            if root.left:
                dfs(root.left, root_sum)
            if root.right:
                dfs(root.right, root_sum)
            self.lookup[root_sum + targetSum] -= 1

        dfs(root, 0)
        return self.ans
