from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    a1, b1 = 2, [3]
    assert sol.superPow(a1, b1) == 8, f"Test case 1 failed: {sol.superPow(a1, b1)}"
    print("Test case 1 passed")
    
    # Example 2
    a2, b2 = 2, [1, 0]
    assert sol.superPow(a2, b2) == 1024, f"Test case 2 failed: {sol.superPow(a2, b2)}"
    print("Test case 2 passed")
    
    # Example 3
    a3, b3 = 1, [4, 3, 3, 8, 5, 2]
    assert sol.superPow(a3, b3) == 1, f"Test case 3 failed: {sol.superPow(a3, b3)}"
    print("Test case 3 passed")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
