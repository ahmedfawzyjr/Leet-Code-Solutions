from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    k1, n1 = 3, 7
    expected1 = [[1, 2, 4]]
    # Sort inner lists and outer list for comparison
    res1 = sol.combinationSum3(k1, n1)
    res1 = sorted([sorted(x) for x in res1])
    expected1 = sorted([sorted(x) for x in expected1])
    assert res1 == expected1, f"Test 1 Failed: {res1}"
    print("Test 1 Passed")

    # Example 2
    k2, n2 = 3, 9
    expected2 = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    res2 = sol.combinationSum3(k2, n2)
    res2 = sorted([sorted(x) for x in res2])
    expected2 = sorted([sorted(x) for x in expected2])
    assert res2 == expected2, f"Test 2 Failed: {res2}"
    print("Test 2 Passed")

    # Example 3
    k3, n3 = 4, 1
    expected3 = []
    res3 = sol.combinationSum3(k3, n3)
    assert res3 == expected3, f"Test 3 Failed: {res3}"
    print("Test 3 Passed")

    # Edge case: no solution
    k4, n4 = 2, 18 # Max sum of 2 numbers is 8+9=17
    expected4 = []
    res4 = sol.combinationSum3(k4, n4)
    assert res4 == expected4, f"Test 4 Failed: {res4}"
    print("Test 4 Passed")

if __name__ == "__main__":
    test_solution()
