class Solution:
    """
    3783. Mirror Distance of an Integer
    Difficulty: Easy

    The mirror distance of an integer n is defined as the absolute difference 
    between n and the number formed by reversing its digits.

    Example:
    Input: n = 25
    Output: 27
    Explanation: reverse(25) = 52. abs(25 - 52) = 27.
    """
    def mirrorDistance(self, n: int) -> int:
        # Handle the case where n is negative if necessary, 
        # though LeetCode problems like this usually involve non-negative integers.
        # If n is negative, the "reversing digits" definition usually applies 
        # to the absolute value or has specific rules.
        # Assuming n >= 0 based on the example.
        
        # Convert to string, reverse, and convert back to integer
        # Leading zeros are naturally handled by int()
        reversed_n = int(str(n)[::-1])
        
        # Return the absolute difference
        return abs(n - reversed_n)

# Example usage/testing:
if __name__ == "__main__":
    sol = Solution()
    print(f"n=25, output={sol.mirrorDistance(25)}")  # Should be 27
    print(f"n=123, output={sol.mirrorDistance(123)}") # 123 -> 321, abs(123-321) = 198
    print(f"n=100, output={sol.mirrorDistance(100)}") # 100 -> 1, abs(100-1) = 99
