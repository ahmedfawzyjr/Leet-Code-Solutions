from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    matrix1 = [[1, 0, 1], [0, -2, 3]]
    k1 = 2
    assert sol.maxSumSubmatrix(matrix1, k1) == 2, f"Test case 1 failed: {sol.maxSumSubmatrix(matrix1, k1)}"
    print("Test case 1 passed")
    
    # Example 2
    matrix2 = [[2, 2, -1]]
    k2 = 3
    assert sol.maxSumSubmatrix(matrix2, k2) == 3, f"Test case 2 failed: {sol.maxSumSubmatrix(matrix2, k2)}"
    print("Test case 2 passed")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
