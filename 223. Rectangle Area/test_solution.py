from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    ax1, ay1, ax2, ay2 = -3, 0, 3, 4
    bx1, by1, bx2, by2 = 0, -1, 9, 2
    expected1 = 45
    assert sol.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) == expected1, f"Test 1 Failed: {sol.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)}"
    print("Test 1 Passed")

    # Example 2
    ax1, ay1, ax2, ay2 = -2, -2, 2, 2
    bx1, by1, bx2, by2 = -2, -2, 2, 2
    expected2 = 16
    assert sol.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) == expected2, f"Test 2 Failed: {sol.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)}"
    print("Test 2 Passed")

    # Edge case: No overlap
    ax1, ay1, ax2, ay2 = 0, 0, 1, 1
    bx1, by1, bx2, by2 = 2, 2, 3, 3
    expected3 = 2
    assert sol.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) == expected3, f"Test 3 Failed: {sol.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)}"
    print("Test 3 Passed")

    # Edge case: One inside another
    ax1, ay1, ax2, ay2 = 0, 0, 10, 10
    bx1, by1, bx2, by2 = 2, 2, 5, 5
    expected4 = 100
    assert sol.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) == expected4, f"Test 4 Failed: {sol.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)}"
    print("Test 4 Passed")

if __name__ == "__main__":
    test_solution()
