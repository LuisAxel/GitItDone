# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        c1, c2 = root.left, root.right

        while c1 and c2:
            #Check value
            if c1.val != c2.val:
                return False

            # Move to right child if left not found
            # Move to left child if right not found
            if c1.left is None and c2.right is None:
                c1 = c1.right
                c2 = c2.left

            # Find most right child of left
            # Find most left child of right
            else:
                # Not same tree
                if (not c1.left and c2.right) or (c1.left and not c2.right):
                    return False

                prev1 = c1.left
                prev2 = c2.right

                while prev1.right and prev1.right is not c1:
                    prev1 = prev1.right
                while prev2.left and prev2.left is not c2:
                    prev2 = prev2.left

                if prev1.right is None and prev2.left is None:
                    prev1.right = c1
                    prev2.left = c2
                    c1 = c1.left
                    c2 = c2.right

                elif prev1.right is c1 and prev2.left is c2:
                    prev1.right = None
                    prev2.left = None
                    c1 = c1.right
                    c2 = c2.left

                # Not same tree
                else:
                    return False


        # One tree could be missing its root
        if (not c1 and c2) or (c1 and not c2):
            return False

        return True
