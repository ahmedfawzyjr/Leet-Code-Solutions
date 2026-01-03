class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Generate the nth element of the count-and-say sequence.
        
        The sequence is defined by:
        - countAndSay(1) = "1"
        - countAndSay(n) = RLE (run-length encoding) of countAndSay(n-1)
        
        Run-length encoding: Replace consecutive identical characters with
        the count followed by the character.
        
        Time Complexity: O(n * m) where m is the length of the resulting string
        Space Complexity: O(m) for storing the current string
        """
        # Base case
        result = "1"
        
        for _ in range(n - 1):
            result = self._run_length_encode(result)
        
        return result
    
    def _run_length_encode(self, s: str) -> str:
        """
        Perform run-length encoding on a string.
        E.g., "1211" -> "111221" (one 1, one 2, two 1s)
        """
        encoded = []
        i = 0
        
        while i < len(s):
            char = s[i]
            count = 1
            
            # Count consecutive identical characters
            while i + count < len(s) and s[i + count] == char:
                count += 1
            
            # Append count and character
            encoded.append(str(count))
            encoded.append(char)
            
            i += count
        
        return ''.join(encoded)
