from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    x1, y1, target1 = 3, 5, 4
    assert sol.canMeasureWater(x1, y1, target1) == True, f"Test case 1 failed: {sol.canMeasureWater(x1, y1, target1)}"
    print("Test case 1 passed")
    
    # Example 2
    x2, y2, target2 = 2, 6, 5
    assert sol.canMeasureWater(x2, y2, target2) == False, f"Test case 2 failed: {sol.canMeasureWater(x2, y2, target2)}"
    print("Test case 2 passed")
    
    # Example 3
    x3, y3, target3 = 1, 2, 3
    assert sol.canMeasureWater(x3, y3, target3) == True, f"Test case 3 failed: {sol.canMeasureWater(x3, y3, target3)}"
    print("Test case 3 passed")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
