class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Multiply two non-negative integers represented as strings.
        
        Simulate grade-school multiplication:
        - For digits at positions i and j, their product contributes to positions i+j and i+j+1
        
        Time Complexity: O(m * n) where m, n are lengths of num1, num2
        Space Complexity: O(m + n)
        """
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        # Result can have at most m + n digits
        result = [0] * (m + n)
        
        # Multiply each digit from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Multiply digits
                product = int(num1[i]) * int(num2[j])
                
                # Positions in result array
                p1, p2 = i + j, i + j + 1
                
                # Add to existing value at position p2
                total = product + result[p2]
                
                # Update positions
                result[p2] = total % 10
                result[p1] += total // 10
        
        # Convert to string, skipping leading zeros
        result_str = ""
        for digit in result:
            if not (result_str == "" and digit == 0):
                result_str += str(digit)
        
        return result_str if result_str else "0"


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: num1 = "2", num2 = "3" -> Output: "6"
    print(sol.multiply("2", "3"))  # "6"
    
    # Example 2: num1 = "123", num2 = "456" -> Output: "56088"
    print(sol.multiply("123", "456"))  # "56088"
    
    # Edge cases
    print(sol.multiply("0", "0"))  # "0"
    print(sol.multiply("999", "999"))  # "998001"
