# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        q = []
        q.append([root, root.val])
        curSum = 0

        while q:
            cur, curSum = q.pop()
            if curSum == targetSum and (not cur.left and not cur.right):
                return True

            if cur.right:
                q.append([cur.right, curSum + cur.right.val])
            if cur.left:
                q.append([cur.left, curSum + cur.left.val])
        return False
