# Mocking the guess API
PICKED = 0

def guess(num: int) -> int:
    if num > PICKED:
        return -1
    elif num < PICKED:
        return 1
    else:
        return 0

# Injecting guess into builtins so Solution can see it
import builtins
builtins.guess = guess

from solution import Solution

def test_solution():
    sol = Solution()
    global PICKED
    
    # Example 1
    n1 = 10
    PICKED = 6
    assert sol.guessNumber(n1) == 6, f"Test case 1 failed: {sol.guessNumber(n1)}"
    print("Test case 1 passed")
    
    # Example 2
    n2 = 1
    PICKED = 1
    assert sol.guessNumber(n2) == 1, f"Test case 2 failed: {sol.guessNumber(n2)}"
    print("Test case 2 passed")
    
    # Example 3
    n3 = 2
    PICKED = 1
    assert sol.guessNumber(n3) == 1, f"Test case 3 failed: {sol.guessNumber(n3)}"
    print("Test case 3 passed")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
