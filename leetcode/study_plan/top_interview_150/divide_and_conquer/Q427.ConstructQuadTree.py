"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def checkQuad(grid, row, col, n):
            for r in range(row, row + n):
                for c in range(col, col + n):
                    if grid[row][col] != grid[r][c]:
                        return False
            return True

        def quadTreeBuilder(grid, row, col, n):
            if checkQuad(grid, row, col, n):
                return Node(grid[row][col] == 1, True)

            root = Node(True, False)
            root.topLeft     = quadTreeBuilder(grid, row         , col         , n // 2)
            root.topRight    = quadTreeBuilder(grid, row         , col + n // 2, n // 2)
            root.bottomLeft  = quadTreeBuilder(grid, row + n // 2, col         , n // 2)
            root.bottomRight = quadTreeBuilder(grid, row + n // 2, col + n // 2, n // 2)

            return root

        return quadTreeBuilder(grid, 0, 0, len(grid))
