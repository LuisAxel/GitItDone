# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None

        q = deque()
        q.append(root)
        cur = None
        ans = []
        lvl = 1   # Nodes this lvl
        n_lvl = 0 # Nodes next lvl
        while q:
            ans.append(q[-1].val)
            n_lvl = 0
            for i in range(lvl):
                cur = q.popleft()
                if cur.left:
                    n_lvl += 1
                    q.append(cur.left)
                if cur.right:
                    n_lvl += 1
                    q.append(cur.right)
            lvl = n_lvl
        return ans
