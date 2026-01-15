class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result.append(chr(65 + remainder))
            columnNumber //= 26
        return "".join(reversed(result))

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(f"Example 1 Output: {sol.convertToTitle(1)}") # Expected: "A"
    
    # Example 2
    print(f"Example 2 Output: {sol.convertToTitle(28)}") # Expected: "AB"
    
    # Example 3
    print(f"Example 3 Output: {sol.convertToTitle(701)}") # Expected: "ZY"
