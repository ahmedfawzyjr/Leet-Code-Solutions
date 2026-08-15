from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    buildings1 = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    expected1 = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    assert sol.getSkyline(buildings1) == expected1, f"Test 1 Failed: {sol.getSkyline(buildings1)}"
    print("Test 1 Passed")

    # Example 2
    buildings2 = [[0,2,3],[2,5,3]]
    expected2 = [[0,3],[5,0]]
    assert sol.getSkyline(buildings2) == expected2, f"Test 2 Failed: {sol.getSkyline(buildings2)}"
    print("Test 2 Passed")

    # Edge case: single building
    buildings3 = [[1, 2, 1]]
    expected3 = [[1, 1], [2, 0]]
    assert sol.getSkyline(buildings3) == expected3, f"Test 3 Failed: {sol.getSkyline(buildings3)}"
    print("Test 3 Passed")

    # Edge case: nested buildings
    buildings4 = [[1, 5, 10], [2, 4, 15]]
    expected4 = [[1, 10], [2, 15], [4, 10], [5, 0]]
    assert sol.getSkyline(buildings4) == expected4, f"Test 4 Failed: {sol.getSkyline(buildings4)}"
    print("Test 4 Passed")

if __name__ == "__main__":
    test_solution()
