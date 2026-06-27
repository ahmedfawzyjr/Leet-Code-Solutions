class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        Finds the smallest integer with the same digits that is greater than n.
        Returns -1 if no such integer exists or if it exceeds the 32-bit signed integer limit.
        
        Time Complexity: O(log10(n)) - the number of digits in n is at most 10.
        Space Complexity: O(log10(n)) - to store the digits of n.
        """
        digits = list(str(n))
        length = len(digits)
        
        # Step 1: Find the first decreasing digit from the right
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
            
        # If no such digit is found, the digits are sorted in descending order
        if i < 0:
            return -1
            
        # Step 2: Find the smallest digit greater than digits[i] from the right
        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1
            
        # Step 3: Swap digits[i] and digits[j]
        digits[i], digits[j] = digits[j], digits[i]
        
        # Step 4: Reverse the suffix starting at i + 1
        left, right = i + 1, length - 1
        while left < right:
            digits[left], digits[right] = digits[right], digits[left]
            left += 1
            right -= 1
            
        val = int("".join(digits))
        
        # Check if the result fits in a 32-bit signed integer
        if val > 2**31 - 1:
            return -1
            
        return val
