from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Finds the length of the longest common prefix between any pair of integers 
        (x, y) where x is from arr1 and y is from arr2.
        
        Complexity:
        - Time: O(N * log10(M) + K * log10(M)), where N = len(arr1), K = len(arr2), 
                and M is the maximum value in the arrays.
        - Space: O(N * log10(M)) to store the prefixes.
        """
        prefixes = set()
        
        # Store all possible prefixes of each number in arr1
        for num in arr1:
            while num > 0:
                prefixes.add(num)
                num //= 10
        
        max_len = 0
        
        # Check all possible prefixes of each number in arr2
        for num in arr2:
            while num > 0:
                if num in prefixes:
                    # If prefix is found, it's the longest prefix for this num in arr2
                    # because we are checking from longest to shortest.
                    length = len(str(num))
                    if length > max_len:
                        max_len = length
                    break
                num //= 10
                
        return max_len
