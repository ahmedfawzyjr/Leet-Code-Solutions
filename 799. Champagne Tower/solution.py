class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # We only need to simulate up to query_row.
        # A glass at row r, glass g contributes its overflow to (r+1, g) and (r+1, g+1).
        
        # Initialize the first row with the total amount poured.
        # We can use a 1D array to save space, updating it row by row.
        # However, for clarity and since query_row < 100, a 2D array is fine.
        tower = [[0.0] * (k + 1) for k in range(query_row + 1)]
        tower[0][0] = float(poured)
        
        for r in range(query_row):
            for g in range(len(tower[r])):
                if tower[r][g] > 1.0:
                    overflow = (tower[r][g] - 1.0) / 2.0
                    tower[r+1][g] += overflow
                    tower[r+1][g+1] += overflow
        
        # The result is capped at 1.0 because a glass can only hold 1.0.
        return min(1.0, tower[query_row][query_glass])

if __name__ == "__main__":
    sol = Solution()
    # Test cases from description
    print(f"Test 1: {sol.champagneTower(1, 1, 1)} (Expected: 0.0)")
    print(f"Test 2: {sol.champagneTower(2, 1, 1)} (Expected: 0.5)")
    print(f"Test 3: {sol.champagneTower(100000009, 33, 17)} (Expected: 1.0)")
