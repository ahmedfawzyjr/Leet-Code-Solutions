class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Iterate from the end of the string to the second character
        for i in range(len(s) - 1, 0, -1):
            if int(s[i]) + carry == 1:
                # Number is odd
                # Step 1: Add 1 (becomes even)
                # Step 2: Divide by 2
                steps += 2
                carry = 1
            else:
                # Number is even
                # Step 1: Divide by 2
                steps += 1
                # carry remains the same (0 if s[i] was 0, 1 if s[i] was 1 and carry was 1)
        
        return steps + carry
