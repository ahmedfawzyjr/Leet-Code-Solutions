from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        Assigns cookies to children to maximize the number of content children.
        
        Time complexity: O(n log n + m log m) where n is number of children and m is number of cookies.
        Space complexity: O(1) or O(log n + log m) depending on sorting implementation.
        """
        g.sort()
        s.sort()
        
        child_i = 0
        cookie_j = 0
        
        while child_i < len(g) and cookie_j < len(s):
            # If the current cookie can satisfy the current child's greed
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            # Move to the next cookie regardless
            cookie_j += 1
            
        return child_i
