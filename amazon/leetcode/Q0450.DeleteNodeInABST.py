# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(cur):
            if not cur.left:
                return cur.right
            if not cur.right:
                return cur.left

            replace = cur.right
            while replace.left:
                replace = replace.left

            replace.left = cur.left

            return cur.right


        if not root:
            return None

        if root.val == key:
            return delete(root)

        head = root
        while root:
            if root.val > key:
                if root.left and root.left.val == key:
                    root.left = delete(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = delete(root.right)
                    break
                else:
                    root = root.right

        return head
