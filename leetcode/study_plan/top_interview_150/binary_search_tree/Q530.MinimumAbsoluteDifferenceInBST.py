# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        s = []
        cur = root
        ans, prev = float(inf), float(-inf)

        while cur or s:
            # Append next inorder (leftmost leaf)
            while cur:
                s.append(cur)
                cur = cur.left

            cur = s.pop()
            ans = min(cur.val - prev, ans)
            prev = cur.val
            cur = cur.right

        return ans
