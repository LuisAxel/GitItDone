# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        q = deque()
        ans = []

        q.append(root)

        while q:
            n = len(q)

            for i in range(n):
                cur = q.popleft()
                if i == 0:
                    ans.append(cur.val)
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)

        return ans
