from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    grid1 = [["X","Y","."],["Y",".","."]]
    result1 = sol.numberOfSubmatrices(grid1)
    print(f"Example 1: {result1}")
    assert result1 == 3
    
    # Example 2
    grid2 = [["X","X"],["X","Y"]]
    result2 = sol.numberOfSubmatrices(grid2)
    print(f"Example 2: {result2}")
    assert result2 == 0
    
    # Example 3
    grid3 = [[".",".","."], [".",".","."]]
    result3 = sol.numberOfSubmatrices(grid3)
    print(f"Example 3: {result3}")
    assert result3 == 0

if __name__ == "__main__":
    test_solution()
