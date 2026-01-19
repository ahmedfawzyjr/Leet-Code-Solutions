from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    s1 = "aacecaaa"
    expected1 = "aaacecaaa"
    assert sol.shortestPalindrome(s1) == expected1, f"Test 1 Failed: {sol.shortestPalindrome(s1)}"
    print("Test 1 Passed")

    # Example 2
    s2 = "abcd"
    expected2 = "dcbabcd"
    assert sol.shortestPalindrome(s2) == expected2, f"Test 2 Failed: {sol.shortestPalindrome(s2)}"
    print("Test 2 Passed")

    # Edge case: empty string
    s3 = ""
    expected3 = ""
    assert sol.shortestPalindrome(s3) == expected3, f"Test 3 Failed: {sol.shortestPalindrome(s3)}"
    print("Test 3 Passed")

    # Edge case: single char
    s4 = "a"
    expected4 = "a"
    assert sol.shortestPalindrome(s4) == expected4, f"Test 4 Failed: {sol.shortestPalindrome(s4)}"
    print("Test 4 Passed")

if __name__ == "__main__":
    test_solution()
