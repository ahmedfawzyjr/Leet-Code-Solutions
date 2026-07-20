from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        Shifts a 2D grid of size m x n by k positions.
        
        Strategy:
        Flatten the 2D grid into a 1D list, apply right shift by k % (m * n) positions using slicing,
        and reconstruct the 2D grid.
        
        Time Complexity: O(m * n) - visiting each element to flatten and rebuild grid
        Space Complexity: O(m * n) - storing the 1D list and output grid
        """
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total
        
        if k == 0:
            return grid
        
        # Flatten grid
        flat = [val for row in grid for val in row]
        
        # Shift right by k
        shifted = flat[-k:] + flat[:-k]
        
        # Reconstruct 2D grid
        return [shifted[i * n : (i + 1) * n] for i in range(m)]


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    grid1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k1 = 1
    print(f"Example 1: {sol.shiftGrid(grid1, k1)}")
    # Expected: [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
    
    # Example 2
    grid2 = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
    k2 = 4
    print(f"Example 2: {sol.shiftGrid(grid2, k2)}")
    # Expected: [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]
    
    # Example 3
    grid3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k3 = 9
    print(f"Example 3: {sol.shiftGrid(grid3, k3)}")
    # Expected: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
