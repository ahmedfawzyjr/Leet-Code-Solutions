from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    nums1 = [1,2,3,1]
    indexDiff1 = 3
    valueDiff1 = 0
    expected1 = True
    assert sol.containsNearbyAlmostDuplicate(nums1, indexDiff1, valueDiff1) == expected1, f"Test 1 Failed: {sol.containsNearbyAlmostDuplicate(nums1, indexDiff1, valueDiff1)}"
    print("Test 1 Passed")

    # Example 2
    nums2 = [1,5,9,1,5,9]
    indexDiff2 = 2
    valueDiff2 = 3
    expected2 = False
    assert sol.containsNearbyAlmostDuplicate(nums2, indexDiff2, valueDiff2) == expected2, f"Test 2 Failed: {sol.containsNearbyAlmostDuplicate(nums2, indexDiff2, valueDiff2)}"
    print("Test 2 Passed")

    # Edge case: valueDiff large
    nums3 = [1, 10]
    indexDiff3 = 1
    valueDiff3 = 10
    expected3 = True
    assert sol.containsNearbyAlmostDuplicate(nums3, indexDiff3, valueDiff3) == expected3, f"Test 3 Failed: {sol.containsNearbyAlmostDuplicate(nums3, indexDiff3, valueDiff3)}"
    print("Test 3 Passed")

    # Edge case: negative numbers
    nums4 = [-1, -1]
    indexDiff4 = 1
    valueDiff4 = 0
    expected4 = True
    assert sol.containsNearbyAlmostDuplicate(nums4, indexDiff4, valueDiff4) == expected4, f"Test 4 Failed: {sol.containsNearbyAlmostDuplicate(nums4, indexDiff4, valueDiff4)}"
    print("Test 4 Passed")

if __name__ == "__main__":
    test_solution()
