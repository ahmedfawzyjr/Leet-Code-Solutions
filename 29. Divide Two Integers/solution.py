class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Divide two integers without using multiplication, division, or mod.
        Truncates toward zero and handles 32-bit signed integer overflow.
        
        Uses bit manipulation with exponential search:
        - Double the divisor using left shift until it exceeds dividend
        - Subtract the largest multiple and accumulate the quotient
        
        Time Complexity: O(log^2 n)
        Space Complexity: O(1)
        """
        # Handle overflow case
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign of result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive numbers
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        
        while dividend >= divisor:
            # Find the largest double of divisor that fits
            temp_divisor = divisor
            multiple = 1
            
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            # Subtract and add to quotient
            dividend -= temp_divisor
            quotient += multiple
        
        return -quotient if negative else quotient
