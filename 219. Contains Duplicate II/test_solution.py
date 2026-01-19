from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    nums1 = [1,2,3,1]
    k1 = 3
    expected1 = True
    assert sol.containsNearbyDuplicate(nums1, k1) == expected1, f"Test 1 Failed: {sol.containsNearbyDuplicate(nums1, k1)}"
    print("Test 1 Passed")

    # Example 2
    nums2 = [1,0,1,1]
    k2 = 1
    expected2 = True
    assert sol.containsNearbyDuplicate(nums2, k2) == expected2, f"Test 2 Failed: {sol.containsNearbyDuplicate(nums2, k2)}"
    print("Test 2 Passed")

    # Example 3
    nums3 = [1,2,3,1,2,3]
    k3 = 2
    expected3 = False
    assert sol.containsNearbyDuplicate(nums3, k3) == expected3, f"Test 3 Failed: {sol.containsNearbyDuplicate(nums3, k3)}"
    print("Test 3 Passed")

    # Edge case: empty array
    nums4 = []
    k4 = 0
    expected4 = False
    assert sol.containsNearbyDuplicate(nums4, k4) == expected4, f"Test 4 Failed: {sol.containsNearbyDuplicate(nums4, k4)}"
    print("Test 4 Passed")

if __name__ == "__main__":
    test_solution()
