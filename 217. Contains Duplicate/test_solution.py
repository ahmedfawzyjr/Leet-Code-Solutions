from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    nums1 = [1,2,3,1]
    expected1 = True
    assert sol.containsDuplicate(nums1) == expected1, f"Test 1 Failed: {sol.containsDuplicate(nums1)}"
    print("Test 1 Passed")

    # Example 2
    nums2 = [1,2,3,4]
    expected2 = False
    assert sol.containsDuplicate(nums2) == expected2, f"Test 2 Failed: {sol.containsDuplicate(nums2)}"
    print("Test 2 Passed")

    # Example 3
    nums3 = [1,1,1,3,3,4,3,2,4,2]
    expected3 = True
    assert sol.containsDuplicate(nums3) == expected3, f"Test 3 Failed: {sol.containsDuplicate(nums3)}"
    print("Test 3 Passed")

    # Edge case: empty array
    nums4 = []
    expected4 = False
    assert sol.containsDuplicate(nums4) == expected4, f"Test 4 Failed: {sol.containsDuplicate(nums4)}"
    print("Test 4 Passed")

if __name__ == "__main__":
    test_solution()
