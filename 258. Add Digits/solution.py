class Solution:
    def addDigits(self, num: int) -> int:
        """
        Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
        Follow up: Could you do it without any loop/recursion in O(1) runtime?
        """
        if num == 0:
            return 0
        return 1 + (num - 1) % 9

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    num = 38
    result = sol.addDigits(num)
    print(f"Num: {num}, Result: {result} (Expected: 2)")
    
    # Test Case 2
    num = 0
    result = sol.addDigits(num)
    print(f"Num: {num}, Result: {result} (Expected: 0)")
