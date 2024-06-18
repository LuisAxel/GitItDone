# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        s = []
        cur = root
        prev = float(-inf)

        while cur or s:
            # Append next inorder (leftmost leaf)
            while cur:
                s.append(cur)
                cur = cur.left

            cur = s.pop()
            if prev >= cur.val:
                return False
            prev = cur.val
            cur = cur.right

        return True
