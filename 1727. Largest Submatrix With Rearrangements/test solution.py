from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    matrix1 = [[0,0,1],[1,1,1],[1,0,1]]
    output1 = 4
    result1 = sol.largestSubmatrix(matrix1)
    print(f"Example 1: Expected {output1}, Got {result1}")
    assert result1 == output1
    
    # Example 2
    matrix2 = [[1,0,1,0,1]]
    output2 = 3
    result2 = sol.largestSubmatrix(matrix2)
    print(f"Example 2: Expected {output2}, Got {result2}")
    assert result2 == output2
    
    # Example 3
    matrix3 = [[1,1,0],[1,0,1]]
    output3 = 2
    result3 = sol.largestSubmatrix(matrix3)
    print(f"Example 3: Expected {output3}, Got {result3}")
    assert result3 == output3
    
    print("All tests passed!")

if __name__ == "__main__":
    test_solution()
