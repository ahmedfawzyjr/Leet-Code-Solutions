class Solution:
    def checkDivisibility(self, n: int) -> bool:
        """
        Determines whether n is divisible by the sum of its digit sum and digit product.

        Complexity:
        - Time: O(log10(n)) - We iterate through the digits of n (at most 7 digits for n <= 10^6).
        - Space: O(1) - Only a few integer variables are used.
        """
        digit_sum = 0
        digit_prod = 1
        temp = n
        
        while temp > 0:
            digit = temp % 10
            digit_sum += digit
            digit_prod *= digit
            temp //= 10
            
        total = digit_sum + digit_prod
        return n % total == 0


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: n = 99 -> True
    # digit_sum = 18, digit_prod = 81, total = 99, 99 % 99 == 0
    assert sol.checkDivisibility(99) is True, "Failed on n = 99"
    
    # Example 2: n = 23 -> False
    # digit_sum = 5, digit_prod = 6, total = 11, 23 % 11 != 0
    assert sol.checkDivisibility(23) is False, "Failed on n = 23"
    
    # Additional edge cases:
    # n = 1: digit_sum = 1, digit_prod = 1, total = 2 -> 1 % 2 != 0 -> False
    assert sol.checkDivisibility(1) is False, "Failed on n = 1"
    
    # n = 10: digit_sum = 1, digit_prod = 0, total = 1 -> 10 % 1 == 0 -> True
    assert sol.checkDivisibility(10) is True, "Failed on n = 10"
    
    # n = 1000000: digit_sum = 1, digit_prod = 0, total = 1 -> 1000000 % 1 == 0 -> True
    assert sol.checkDivisibility(1000000) is True, "Failed on n = 1000000"
    
    print("All test cases passed successfully!")
