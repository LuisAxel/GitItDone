# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        q = deque()
        max_sum = float('-inf')
        max_lvl = 1
        cur_lvl = 0

        q.append(root)

        while q:
            n = len(q)
            lvl_sum = 0
            cur_lvl += 1
            for i in range(n):
                cur = q.popleft()
                lvl_sum += cur.val

                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)

            if lvl_sum > max_sum:
                max_lvl = cur_lvl
                max_sum = lvl_sum

        return max_lvl
