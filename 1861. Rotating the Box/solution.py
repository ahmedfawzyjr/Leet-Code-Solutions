from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        """
        Rotates the box 90 degrees clockwise and applies gravity to stones.
        
        Strategy:
        1. Process each row to simulate gravity horizontally (towards the right end).
           - Iterate from right to left in each row.
           - Maintain an 'empty' pointer indicating the next available spot for a stone.
           - If a stone '#' is found, move it to the 'empty' spot and update the pointer.
           - If an obstacle '*' is found, reset the 'empty' pointer to the spot before it.
        2. Rotate the grid 90 degrees clockwise.
           - Cell (r, c) in original m x n grid moves to (c, m-1-r) in new n x m grid.
           
        Time Complexity: O(m * n) - where m is number of rows and n is number of columns.
        Space Complexity: O(m * n) - for the result matrix.
        """
        m = len(boxGrid)
        n = len(boxGrid[0])
        
        # Step 1: Apply gravity to each row (simulated horizontally)
        for r in range(m):
            empty = n - 1
            for c in range(n - 1, -1, -1):
                if boxGrid[r][c] == '#':
                    # Move stone to the furthest possible empty spot
                    boxGrid[r][c] = '.'
                    boxGrid[r][empty] = '#'
                    empty -= 1
                elif boxGrid[r][c] == '*':
                    # Obstacle resets the gravity target spot
                    empty = c - 1
        
        # Step 2: Rotate the matrix 90 degrees clockwise
        res = [['' for _ in range(m)] for _ in range(n)]
        for r in range(m):
            for c in range(n):
                res[c][m - 1 - r] = boxGrid[r][c]
                
        return res


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    box1 = [["#",".","#"]]
    print(sol.rotateTheBox(box1))
    # Output: [["."],["#"],["#"]]
    
    # Example 2
    box2 = [["#",".","*","."],
            ["#","#","*","."]]
    print(sol.rotateTheBox(box2))
    # Output: [["#","."],["#","#"],["*","*"],[".", "."]]
    
    # Example 3
    box3 = [["#","#","*",".","*","."],
            ["#","#","#","*",".","."],
            ["#","#","#",".","#","."]]
    print(sol.rotateTheBox(box3))
    # Output: [[".",".","#"],[".","#","#"],["#","#","#"],["#","*","."],["#",".","*"],["#",".","."]]
