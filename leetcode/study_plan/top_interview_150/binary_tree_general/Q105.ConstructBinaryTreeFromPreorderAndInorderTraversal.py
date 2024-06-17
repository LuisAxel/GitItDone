# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        idx = {}
        for i, v in enumerate(inorder):
            idx[v] = i

        def build(p_start, p_end, i_start, size):
            if p_start > p_end:
                return None

            new = TreeNode(preorder[p_start])
            i_idx = idx[preorder[p_start]]

            l_size = i_idx - i_start
            r_size = size - l_size - 1

            new.left = build(p_start + 1, p_start + l_size, i_start, l_size)

            new.right = build(p_start + l_size + 1, p_end, i_idx + 1, r_size)

            return new

        return build(0, n - 1, 0, n -1)
