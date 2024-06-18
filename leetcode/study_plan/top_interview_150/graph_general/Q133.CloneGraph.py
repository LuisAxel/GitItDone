"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        q = deque([node])
        clones = {node.val : Node(node.val)}

        while q:
            cur = q.popleft()
            clone = clones[cur.val]

            for neigh in cur.neighbors:
                if neigh.val not in clones:
                    clones[neigh.val] = Node(neigh.val)
                    q.append(neigh)
                clone.neighbors.append(clones[neigh.val])

        return clones[1]
