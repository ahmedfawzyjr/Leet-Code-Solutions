from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    nums1 = [3,2,1,5,6,4]
    k1 = 2
    expected1 = 5
    assert sol.findKthLargest(nums1, k1) == expected1, f"Test 1 Failed: {sol.findKthLargest(nums1, k1)}"
    print("Test 1 Passed")

    # Example 2
    nums2 = [3,2,3,1,2,4,5,5,6]
    k2 = 4
    expected2 = 4
    assert sol.findKthLargest(nums2, k2) == expected2, f"Test 2 Failed: {sol.findKthLargest(nums2, k2)}"
    print("Test 2 Passed")

    # Edge case: k=1 (max)
    nums3 = [1, 2, 3]
    k3 = 1
    expected3 = 3
    assert sol.findKthLargest(nums3, k3) == expected3, f"Test 3 Failed: {sol.findKthLargest(nums3, k3)}"
    print("Test 3 Passed")

    # Edge case: k=len(nums) (min)
    nums4 = [1, 2, 3]
    k4 = 3
    expected4 = 1
    assert sol.findKthLargest(nums4, k4) == expected4, f"Test 4 Failed: {sol.findKthLargest(nums4, k4)}"
    print("Test 4 Passed")

if __name__ == "__main__":
    test_solution()
