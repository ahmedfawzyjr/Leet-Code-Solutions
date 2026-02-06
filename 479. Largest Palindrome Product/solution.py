class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        
        upper = 10**n - 1
        lower = 10**(n - 1)
        
        # We search from the largest possible palindrome down
        # A palindrome of 2n digits can be formed by concatenating half and its reverse
        for half in range(upper, lower - 1, -1):
            p = int(str(half) + str(half)[::-1])
            
            # Check if this palindrome can be a product of two n-digit numbers
            # start from upper down to sqrt(p)
            for j in range(upper, int(p**0.5), -1):
                if p % j == 0:
                    return p % 1337
                if p // j > upper:
                    break
        return -1
