from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    num1 = 16
    assert sol.isPerfectSquare(num1) == True, f"Test case 1 failed: {num1}"
    print("Test case 1 passed")
    
    # Example 2
    num2 = 14
    assert sol.isPerfectSquare(num2) == False, f"Test case 2 failed: {num2}"
    print("Test case 2 passed")
    
    # Additional test cases
    assert sol.isPerfectSquare(1) == True, "Test case 3 failed: 1"
    assert sol.isPerfectSquare(4) == True, "Test case 4 failed: 4"
    assert sol.isPerfectSquare(25) == True, "Test case 5 failed: 25"
    assert sol.isPerfectSquare(2000105819) == False, "Test case 6 failed: 2000105819"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
