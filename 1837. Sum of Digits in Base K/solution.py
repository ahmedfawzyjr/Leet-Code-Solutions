class Solution:
    def sumBase(self, n: int, k: int) -> int:
        """
        Calculates the sum of digits of `n` after converting it from base 10 to base `k`.

        Approach:
        1. Repeatedly extract the least significant digit in base `k` using `n % k`.
        2. Accumulate the extracted digit into a running sum.
        3. Reduce `n` using integer division `n //= k`.
        4. Repeat until `n` becomes 0.

        Complexity:
        - Time Complexity: O(log_k(n)), where n is the given integer.
        - Space Complexity: O(1) auxiliary space.
        """
        res = 0
        while n > 0:
            res += n % k
            n //= k
        return res


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    # Input: n = 34, k = 6
    # Output: 9
    assert sol.sumBase(34, 6) == 9, f"Failed Example 1: got {sol.sumBase(34, 6)}"

    # Example 2
    # Input: n = 10, k = 10
    # Output: 1
    assert sol.sumBase(10, 10) == 1, f"Failed Example 2: got {sol.sumBase(10, 10)}"

    # Edge cases
    # Single digit in base k
    assert sol.sumBase(5, 6) == 5
    # Largest n constraint (100) in base 2 (100 in base 2 = 1100100 -> 1+1+0+0+1+0+0 = 3)
    assert sol.sumBase(100, 2) == 3
    # n = 100 in base 10 -> 1+0+0 = 1
    assert sol.sumBase(100, 10) == 1

    print("All test cases passed successfully!")
