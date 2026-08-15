from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    assert sol.minNumberOperations([1, 2, 3, 2, 1]) == 3
    
    # Example 2
    assert sol.minNumberOperations([3, 1, 1, 2]) == 4
    
    # Example 3
    assert sol.minNumberOperations([3, 1, 5, 4, 2]) == 7

if __name__ == "__main__":
    test_solution()
    print("All tests passed!")
