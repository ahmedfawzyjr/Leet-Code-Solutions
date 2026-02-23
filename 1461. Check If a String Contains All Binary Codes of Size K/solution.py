class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        Check if a string contains all binary codes of size K.
        We optimize this by first checking if the string is long enough to
        even contain 2^k distinct substrings.
        Then, we use a set to collect all substrings of size K.
        """
        # If the string length is less than the minimum required length
        # to contain 2^k distinct strings of length k, it's impossible.
        if len(s) < (1 << k) + k - 1:
            return False
            
        # Add all substrings of length k to a set. 
        # Sets only keep unique elements.
        unique_substrings = set(s[i:i+k] for i in range(len(s) - k + 1))
        
        # Check if we have exactly 2^k unique substrings
        return len(unique_substrings) == (1 << k)
