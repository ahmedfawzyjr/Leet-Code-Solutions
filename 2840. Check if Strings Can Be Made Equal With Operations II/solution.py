class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # Characters at even indices can only be swapped with characters at even indices.
        # Characters at odd indices can only be swapped with characters at odd indices.
        # This is because the swap condition is j - i is even, meaning i and j must have same parity.
        # So, s1 can be made equal to s2 if and only if:
        # 1. Frequency of characters at even indices in s1 matches that of s2.
        # 2. Frequency of characters at odd indices in s1 matches that of s2.
        
        return sorted(s1[0::2]) == sorted(s2[0::2]) and sorted(s1[1::2]) == sorted(s2[1::2])
