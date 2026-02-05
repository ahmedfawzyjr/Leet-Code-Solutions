class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        Checks if the string can be constructed by taking a substring and appending multiple copies.
        A clever trick: If s is composed of a repeated substring 'P', then s = P+P+...+P.
        If we double the string (s+s) and remove the first and last characters, 
        the original string 's' should still exist in it if it's periodic.
        
        Time complexity: O(n)
        Space complexity: O(n) for the concatenated string.
        """
        if not s:
            return False
            
        ss = (s + s)[1:-1]
        return s in ss
