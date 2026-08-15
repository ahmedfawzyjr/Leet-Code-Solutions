from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    matrix1 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    expected1 = 4
    assert sol.maximalSquare(matrix1) == expected1, f"Test 1 Failed: {sol.maximalSquare(matrix1)}"
    print("Test 1 Passed")

    # Example 2
    matrix2 = [["0","1"],["1","0"]]
    expected2 = 1
    assert sol.maximalSquare(matrix2) == expected2, f"Test 2 Failed: {sol.maximalSquare(matrix2)}"
    print("Test 2 Passed")

    # Example 3
    matrix3 = [["0"]]
    expected3 = 0
    assert sol.maximalSquare(matrix3) == expected3, f"Test 3 Failed: {sol.maximalSquare(matrix3)}"
    print("Test 3 Passed")

    # Edge case: empty matrix
    matrix4 = []
    expected4 = 0
    assert sol.maximalSquare(matrix4) == expected4, f"Test 4 Failed: {sol.maximalSquare(matrix4)}"
    print("Test 4 Passed")

if __name__ == "__main__":
    test_solution()
