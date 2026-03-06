class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        """
        Given a binary string s without leading zeros, return true if s contains 
        at most one contiguous segment of ones. Otherwise, return false.
        
        Constraints:
        - 1 <= s.length <= 100
        - s[i] is either '0' or '1'
        - s[0] is '1'
        
        Logic:
        Since the string has no leading zeros and s[0] is '1', there is at least one 
        segment of ones starting at the beginning.
        If there is more than one segment of ones, it means there must be a '0' followed 
         by a '1' somewhere in the string.
        So, we just need to check if "01" is a substring of s.
        """
        return "01" not in s
