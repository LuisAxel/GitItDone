# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        q = deque()
        q.append(root)
        cur = None
        ans = []
        sum_lvl = root.val
        lvl = 1   # Nodes this lvl
        n_lvl = 0 # Nodes next lvl
        while q:
            ans.append(sum_lvl / lvl)
            n_lvl = 0
            sum_lvl = 0
            for i in range(lvl):
                cur = q.popleft()
                if cur.left:
                    n_lvl += 1
                    sum_lvl += cur.left.val
                    q.append(cur.left)
                if cur.right:
                    n_lvl += 1
                    sum_lvl += cur.right.val
                    q.append(cur.right)
            lvl = n_lvl
        return ans
