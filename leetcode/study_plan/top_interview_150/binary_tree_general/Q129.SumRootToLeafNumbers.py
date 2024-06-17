# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        q = []
        q.append([root, root.val])
        curSum = 0
        ans = 0

        while q:
            cur, curSum = q.pop()
            if (not cur.left and not cur.right):
                ans += curSum

            if cur.right:
                q.append([cur.right, (curSum * 10) + cur.right.val])
            if cur.left:
                q.append([cur.left, (curSum * 10) + cur.left.val])

        return ans
