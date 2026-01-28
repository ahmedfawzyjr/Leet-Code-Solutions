from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    a1, b1 = 1, 2
    assert sol.getSum(a1, b1) == 3, f"Test case 1 failed: {sol.getSum(a1, b1)}"
    print("Test case 1 passed")
    
    # Example 2
    a2, b2 = 2, 3
    assert sol.getSum(a2, b2) == 5, f"Test case 2 failed: {sol.getSum(a2, b2)}"
    print("Test case 2 passed")
    
    # Negative numbers
    a3, b3 = -1, 1
    assert sol.getSum(a3, b3) == 0, f"Test case 3 failed: {sol.getSum(a3, b3)}"
    print("Test case 3 passed")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
