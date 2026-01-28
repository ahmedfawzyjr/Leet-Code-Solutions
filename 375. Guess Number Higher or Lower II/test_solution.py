from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    n1 = 10
    assert sol.getMoneyAmount(n1) == 16, f"Test case 1 failed: {sol.getMoneyAmount(n1)}"
    print("Test case 1 passed")
    
    # Example 2
    n2 = 1
    assert sol.getMoneyAmount(n2) == 0, f"Test case 2 failed: {sol.getMoneyAmount(n2)}"
    print("Test case 2 passed")
    
    # Example 3
    n3 = 2
    assert sol.getMoneyAmount(n3) == 1, f"Test case 3 failed: {sol.getMoneyAmount(n3)}"
    print("Test case 3 passed")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
