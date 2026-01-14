class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = []
        
        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
            
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        # Integer part
        result.append(str(numerator // denominator))
        remainder = numerator % denominator
        
        if remainder == 0:
            return "".join(result)
            
        result.append(".")
        
        # Fractional part
        remainder_map = {}
        
        while remainder != 0:
            if remainder in remainder_map:
                result.insert(remainder_map[remainder], "(")
                result.append(")")
                break
            
            remainder_map[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
            
        return "".join(result)

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    n1, d1 = 1, 2
    print(f"Input: numerator = {n1}, denominator = {d1}")
    print(f"Output: '{solution.fractionToDecimal(n1, d1)}'")
    # Expected: "0.5"
    
    # Example 2
    n2, d2 = 2, 1
    print(f"Input: numerator = {n2}, denominator = {d2}")
    print(f"Output: '{solution.fractionToDecimal(n2, d2)}'")
    # Expected: "2"
    
    # Example 3
    n3, d3 = 4, 333
    print(f"Input: numerator = {n3}, denominator = {d3}")
    print(f"Output: '{solution.fractionToDecimal(n3, d3)}'")
    # Expected: "0.(012)"
