class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Implement pow(x, n) using binary exponentiation.
        
        Key insight: x^n = (x^2)^(n/2) if n is even
                     x^n = x * (x^2)^((n-1)/2) if n is odd
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        if n == 0:
            return 1.0
        
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        
        while n > 0:
            # If n is odd, multiply result by x
            if n % 2 == 1:
                result *= x
            
            # Square x and halve n
            x *= x
            n //= 2
        
        return result
    
    def myPow_recursive(self, x: float, n: int) -> float:
        """
        Alternative: Recursive approach.
        
        Time Complexity: O(log n)
        Space Complexity: O(log n) for recursion stack
        """
        if n == 0:
            return 1.0
        
        if n < 0:
            return 1 / self.myPow_recursive(x, -n)
        
        if n % 2 == 0:
            half = self.myPow_recursive(x, n // 2)
            return half * half
        else:
            return x * self.myPow_recursive(x, n - 1)


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: x = 2.00000, n = 10 -> 1024.00000
    print(sol.myPow(2.0, 10))  # 1024.0
    
    # Example 2: x = 2.10000, n = 3 -> 9.26100
    print(sol.myPow(2.1, 3))  # 9.261
    
    # Example 3: x = 2.00000, n = -2 -> 0.25000
    print(sol.myPow(2.0, -2))  # 0.25
