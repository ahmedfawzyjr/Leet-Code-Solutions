from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    nums1 = [1, 2, 3]
    res1 = sol.largestDivisibleSubset(nums1)
    # [1, 2] or [1, 3] are valid
    assert res1 == [1, 2] or res1 == [1, 3], f"Test case 1 failed: {res1}"
    print("Test case 1 passed")
    
    # Example 2
    nums2 = [1, 2, 4, 8]
    res2 = sol.largestDivisibleSubset(nums2)
    assert res2 == [1, 2, 4, 8], f"Test case 2 failed: {res2}"
    print("Test case 2 passed")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
