# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = []
        cur = root
        seen = 1

        while cur or s:
            # Append next inorder (leftmost leaf)
            while cur:
                s.append(cur)
                cur = cur.left

            cur = s.pop()
            if seen == k:
                return cur.val
            seen += 1
            cur = cur.right

        return -1
