from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def solve(r, c, n):
            # Check if all elements in the current subgrid are the same
            all_same = True
            first_val = grid[r][c]
            for i in range(r, r + n):
                for j in range(c, c + n):
                    if grid[i][j] != first_val:
                        all_same = False
                        break
                if not all_same:
                    break
            
            if all_same:
                return Node(first_val == 1, True)
            
            # Divide into 4 subgrids
            n //= 2
            topLeft = solve(r, c, n)
            topRight = solve(r, c + n, n)
            bottomLeft = solve(r + n, c, n)
            bottomRight = solve(r + n, c + n, n)
            
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
            
        return solve(0, 0, len(grid))
