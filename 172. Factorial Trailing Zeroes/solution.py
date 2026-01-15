class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(f"Example 1 Output: {sol.trailingZeroes(3)}") # Expected: 0
    
    # Example 2
    print(f"Example 2 Output: {sol.trailingZeroes(5)}") # Expected: 1
    
    # Example 3
    print(f"Example 3 Output: {sol.trailingZeroes(0)}") # Expected: 0
