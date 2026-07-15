from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    assert sol.validSquare([0,0], [1,1], [1,0], [0,1]) == True, "Example 1 failed"
    print("Example 1 passed")
    
    # Example 2
    assert sol.validSquare([0,0], [1,1], [1,0], [0,12]) == False, "Example 2 failed"
    print("Example 2 passed")
    
    # Example 3
    assert sol.validSquare([1,0], [-1,0], [0,1], [0,-1]) == True, "Example 3 failed"
    print("Example 3 passed")
    
    # All same points (invalid)
    assert sol.validSquare([0,0], [0,0], [0,0], [0,0]) == False, "All same points failed"
    print("All same points check passed")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
