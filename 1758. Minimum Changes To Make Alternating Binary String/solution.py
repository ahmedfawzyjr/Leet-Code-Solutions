class Solution:
    def minOperations(self, s: str) -> int:
        """
        Calculates the minimum number of bit flips to make a binary string alternating.
        
        Complexity:
        Time: O(n) where n is the length of the string s.
        Space: O(1) as we only use a counter.
        """
        changes_to_type0 = 0  # To match "010101..."
        
        for i, char in enumerate(s):
            # i % 2 == 0: expected '0'
            # i % 2 == 1: expected '1'
            expected = '0' if i % 2 == 0 else '1'
            if char != expected:
                changes_to_type0 += 1
        
        # Total length n, changes for "101010..." = n - changes_to_type0
        n = len(s)
        return min(changes_to_type0, n - changes_to_type0)
