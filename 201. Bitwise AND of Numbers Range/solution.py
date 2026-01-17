class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # Find the common prefix
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(f"Example 1: {sol.rangeBitwiseAnd(5, 7)}") # Expected: 4
    
    # Example 2
    print(f"Example 2: {sol.rangeBitwiseAnd(0, 0)}") # Expected: 0
    
    # Example 3
    print(f"Example 3: {sol.rangeBitwiseAnd(1, 2147483647)}") # Expected: 0
