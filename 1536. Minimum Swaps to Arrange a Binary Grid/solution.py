class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n = len(grid)
        # Calculate trailing zeros for each row
        trailing_zeros = []
        for i in range(n):
            count = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    count += 1
                else:
                    break
            trailing_zeros.append(count)
        
        total_swaps = 0
        for i in range(n):
            # For row i, we need at least n - 1 - i trailing zeros
            target = n - 1 - i
            found = False
            for j in range(i, n):
                if trailing_zeros[j] >= target:
                    # Found a row that can be moved to position i
                    total_swaps += (j - i)
                    # Move the row to index i by shifting other rows down
                    row_to_move = trailing_zeros.pop(j)
                    trailing_zeros.insert(i, row_to_move)
                    found = True
                    break
            
            if not found:
                return -1
                
        return total_swaps
