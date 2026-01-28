from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    nums1_1, nums2_1, k1 = [1, 7, 11], [2, 4, 6], 3
    res1 = sol.kSmallestPairs(nums1_1, nums2_1, k1)
    # Expected: [[1, 2], [1, 4], [1, 6]]
    assert res1 == [[1, 2], [1, 4], [1, 6]], f"Test case 1 failed: {res1}"
    print("Test case 1 passed")
    
    # Example 2
    nums1_2, nums2_2, k2 = [1, 1, 2], [1, 2, 3], 2
    res2 = sol.kSmallestPairs(nums1_2, nums2_2, k2)
    # Expected: [[1, 1], [1, 1]]
    assert res2 == [[1, 1], [1, 1]], f"Test case 2 failed: {res2}"
    print("Test case 2 passed")
    
    # Example 3
    nums1_3, nums2_3, k3 = [1, 2], [3], 3
    res3 = sol.kSmallestPairs(nums1_3, nums2_3, k3)
    # Expected: [[1, 3], [2, 3]]
    assert res3 == [[1, 3], [2, 3]], f"Test case 3 failed: {res3}"
    print("Test case 3 passed")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
