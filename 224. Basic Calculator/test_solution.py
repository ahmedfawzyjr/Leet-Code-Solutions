from solution import Solution

def test_solution():
    sol = Solution()
    
    # Example 1
    s1 = "1 + 1"
    expected1 = 2
    assert sol.calculate(s1) == expected1, f"Test 1 Failed: {sol.calculate(s1)}"
    print("Test 1 Passed")

    # Example 2
    s2 = " 2-1 + 2 "
    expected2 = 3
    assert sol.calculate(s2) == expected2, f"Test 2 Failed: {sol.calculate(s2)}"
    print("Test 2 Passed")

    # Example 3
    s3 = "(1+(4+5+2)-3)+(6+8)"
    expected3 = 23
    assert sol.calculate(s3) == expected3, f"Test 3 Failed: {sol.calculate(s3)}"
    print("Test 3 Passed")

    # Edge case: Unary minus at start (handled by logic implicitly as 0 - ...)
    # But wait, the problem says '-' could be used as unary operation.
    # Example: "-2+ 1" -> -1.
    # My logic: init result=0, sign=1.
    # char '-': result += 1*0 (0), num=0, sign=-1.
    # char '2': num=2.
    # char '+': result += -1*2 (-2), num=0, sign=1.
    # char '1': num=1.
    # end: result += 1*1 (-2+1 = -1). Correct.
    s4 = "-2+ 1"
    expected4 = -1
    assert sol.calculate(s4) == expected4, f"Test 4 Failed: {sol.calculate(s4)}"
    print("Test 4 Passed")
    
    # Edge case: Nested parentheses with unary minus
    # -(2 + 3) = -5
    s5 = "-(2 + 3)"
    expected5 = -5
    assert sol.calculate(s5) == expected5, f"Test 5 Failed: {sol.calculate(s5)}"
    print("Test 5 Passed")

if __name__ == "__main__":
    test_solution()
