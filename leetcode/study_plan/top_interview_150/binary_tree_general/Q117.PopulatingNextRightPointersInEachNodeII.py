"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        candidate = root.next

        # Childs can have a next value if
        # 1. Left can have next = root.right or candidate from 2 (root.right > candidate)
        # 2. Next can be any node (left > right) from root.next
        while candidate:
            if candidate.left:
                candidate = candidate.left
                break
            if candidate.right:
                candidate = candidate.right
                break
            # move to next neighbour
            candidate = candidate.next

        if root.left:
            root.left.next = root.right or candidate
        if root.right:
            root.right.next = candidate

	# Right first to populate next for left
        self.connect(root.right)
        self.connect(root.left)

        return root
