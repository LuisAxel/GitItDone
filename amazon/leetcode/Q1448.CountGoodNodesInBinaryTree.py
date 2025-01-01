# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        s = []
        ans = 0
        s.append([root, root.val])

        while s:
            curr, val = s.pop()
            if curr.val >= val:
                ans += 1

            if curr.right:
                s.append([curr.right, max(curr.val, val)])
            if curr.left:
                s.append([curr.left, max(curr.val, val)])

        return ans
