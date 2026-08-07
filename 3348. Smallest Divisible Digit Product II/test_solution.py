import sys
from solution import Solution

def run_tests():
    sol = Solution()
    
    test_cases = [
        ("1234", 256, "1488"),
        ("12355", 50, "12355"),
        ("11111", 26, "-1"),
        ("123", 1, "123"),
        ("10999", 2, "11112"), # num has '0'
        ("99", 100, "455"), # 2^2 * 5^2 = 100 -> digits 4,5,5 -> product 100 >= 99
    ]
    
    for i, (num, t, expected) in enumerate(test_cases):
        res = sol.smallestNumber(num, t)
        print(f"Test {i+1}: num={num}, t={t} -> Output: '{res}', Expected: '{expected}'")
        assert res == expected, f"Failed on test {i+1}: got {res}, expected {expected}"
        
    print("ALL TESTS PASSED!")

if __name__ == "__main__":
    run_tests()
