from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    n1 = 2
    assert sol.countNumbersWithUniqueDigits(n1) == 91, f"Test case 1 failed: {sol.countNumbersWithUniqueDigits(n1)}"
    print("Test case 1 passed")
    
    # Example 2
    n2 = 0
    assert sol.countNumbersWithUniqueDigits(n2) == 1, f"Test case 2 failed: {sol.countNumbersWithUniqueDigits(n2)}"
    print("Test case 2 passed")
    
    # Additional test cases
    assert sol.countNumbersWithUniqueDigits(1) == 10, "Test case 3 failed: 1"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
