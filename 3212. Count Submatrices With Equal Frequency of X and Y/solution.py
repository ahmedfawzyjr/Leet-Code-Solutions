class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        """
        Calculates the number of submatrices that start at (0, 0) and have an 
        equal frequency of 'X' and 'Y', with at least one 'X'.
        
        Time Complexity: O(R * C) where R is the number of rows and C is the number of columns.
        Space Complexity: O(C) to store the prefix counts of the previous row.
        """
        R = len(grid)
        C = len(grid[0])
        
        # prevX[c+1] stores the number of 'X's in the submatrix from (0, 0) to (r-1, c)
        prevX = [0] * (C + 1)
        prevY = [0] * (C + 1)
        
        ans = 0
        for r in range(R):
            currX = [0] * (C + 1)
            currY = [0] * (C + 1)
            rowX = 0
            rowY = 0
            for c in range(C):
                if grid[r][c] == 'X':
                    rowX += 1
                elif grid[r][c] == 'Y':
                    rowY += 1
                
                # Total counts in submatrix (0,0) to (r,c)
                currX[c+1] = prevX[c+1] + rowX
                currY[c+1] = prevY[c+1] + rowY
                
                # Check conditions: equal X and Y, and at least one X
                if currX[c+1] == currY[c+1] and currX[c+1] > 0:
                    ans += 1
            
            # Update previous row counts for the next iteration
            prevX = currX
            prevY = currY
            
        return ans
