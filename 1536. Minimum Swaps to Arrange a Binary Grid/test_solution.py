from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    grid1 = [[0,0,1],[1,1,0],[1,0,0]]
    result1 = sol.minSwaps(grid1)
    print(f"Example 1: {result1}")
    assert result1 == 3
    
    # Example 2
    grid2 = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
    result2 = sol.minSwaps(grid2)
    print(f"Example 2: {result2}")
    assert result2 == -1
    
    # Example 3
    grid3 = [[1,0,0],[1,1,0],[1,1,1]]
    result3 = sol.minSwaps(grid3)
    print(f"Example 3: {result3}")
    assert result3 == 0

if __name__ == "__main__":
    test_solution()
