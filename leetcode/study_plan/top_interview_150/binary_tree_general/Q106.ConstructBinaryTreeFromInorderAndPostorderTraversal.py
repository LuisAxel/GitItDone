# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        idx = {}
        for i, v in enumerate(inorder):
            idx[v] = i

        def build(p_start, p_end, i_start, size):
            if p_start > p_end:
                return None

            new = TreeNode(postorder[p_end])
            i_idx = idx[postorder[p_end]]

            l_size = i_idx - i_start
            r_size = size - l_size - 1

            new.left = build(p_start, p_start + l_size - 1, i_start, l_size)

            new.right = build(p_start + l_size, p_end - 1, i_idx + 1, r_size)

            return new

        return build(0, n - 1, 0, n -1)
