# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)
        lvl = 1
        n_lvl = 0
        ans = []
        zigzag = True

        while lvl > 0:
            n_lvl = 0
            lvl_val = []
            for i in range(lvl):
                cur = q.popleft()
                lvl_val.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                    n_lvl += 1
                if cur.right:
                    q.append(cur.right)
                    n_lvl += 1
            lvl = n_lvl
            if zigzag:
                ans.append(lvl_val)
            else:
                ans.append(reversed(lvl_val))
            zigzag = not zigzag

        return ans
