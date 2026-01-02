class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Find the index of the first occurrence of needle in haystack.
        Returns -1 if needle is not part of haystack.
        
        Uses Python's built-in find method for simplicity.
        Alternative: implement KMP algorithm for O(n+m) time.
        
        Time Complexity: O(n * m) worst case, O(n + m) with KMP
        Space Complexity: O(1)
        """
        return haystack.find(needle)
    
    def strStr_manual(self, haystack: str, needle: str) -> int:
        """
        Manual implementation using sliding window.
        """
        if not needle:
            return 0
        
        n, m = len(haystack), len(needle)
        
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        
        return -1
