# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def left(cur):
            h = 0
            while cur:
                h += 1
                cur = cur.left
            return h

        def right(cur):
            h = 0
            while cur:
                h += 1
                cur = cur.right
            return h

        def count(cur):
            l_h = left(cur)
            r_h = right(cur)

            if l_h == r_h:
                return (2 ** l_h) - 1

            return 1 + count(cur.left) + count(cur.right)

        return count(root)

# 1 -> 1 -> 2^1 - 1
# 2 -> 3 -> 2^2 - 1
# 3 -> 7 -> 2^3 - 1
# 4 -> 15 -> 2^4 - 1
