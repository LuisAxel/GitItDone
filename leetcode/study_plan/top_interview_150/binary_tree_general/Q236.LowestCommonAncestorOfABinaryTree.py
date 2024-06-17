# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def preorder(cur):
            nonlocal p, q

            if not cur or cur in [p,q]:
                # None or found  P || Q
                return cur

            # None or node with P || Q
            l = preorder(cur.left)
            r = preorder(cur.right)

            # Found both, LCA is cur
            if l and r:
                return cur

            # Found L or R or None
            return l or r

        return preorder(root)
