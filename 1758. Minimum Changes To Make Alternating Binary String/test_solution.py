from solution import Solution

def run_test(s, expected):
    sol = Solution()
    result = sol.minOperations(s)
    status = "PASS" if result == expected else "FAIL"
    print(f"Test case s='{s}': Expected={expected}, Result={result} -> {status}")
    return result == expected

if __name__ == "__main__":
    tests = [
        ("0100", 1),
        ("10", 0),
        ("1111", 2)
    ]
    
    all_passed = True
    for s, expected in tests:
        if not run_test(s, expected):
            all_passed = False
            
    if all_passed:
        print("\nAll tests passed successfully!")
    else:
        print("\nSome tests failed.")
        exit(1)
