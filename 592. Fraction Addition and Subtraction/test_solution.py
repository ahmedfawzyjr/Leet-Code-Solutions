from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    assert sol.fractionAddition("-1/2+1/2") == "0/1", "Example 1 failed"
    print("Example 1 passed")
    
    # Example 2
    assert sol.fractionAddition("-1/2+1/2+1/3") == "1/3", "Example 2 failed"
    print("Example 2 passed")
    
    # Example 3
    assert sol.fractionAddition("1/3-1/2") == "-1/6", "Example 3 failed"
    print("Example 3 passed")
    
    # Extra test case: integer results
    assert sol.fractionAddition("5/3+1/3") == "2/1", "Integer result test failed"
    print("Integer result test passed")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
