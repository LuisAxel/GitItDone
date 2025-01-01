# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(root: TreeNode) -> List:
            s = []
            leaves = []
            s.append(root)

            while s:
                curr = s.pop()
                if curr.right:
                    s.append(curr.right)
                if curr.left:
                    s.append(curr.left)

                if not curr.right and not curr.left:
                    leaves.append(curr.val)

            return leaves

        leaf1 = helper(root1)
        leaf2 = helper(root2)

        return leaf1 == leaf2
