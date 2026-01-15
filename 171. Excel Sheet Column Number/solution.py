class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(f"Example 1 Output: {sol.titleToNumber('A')}") # Expected: 1
    
    # Example 2
    print(f"Example 2 Output: {sol.titleToNumber('AB')}") # Expected: 28
    
    # Example 3
    print(f"Example 3 Output: {sol.titleToNumber('ZY')}") # Expected: 701
