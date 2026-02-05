from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Sorts the characters of a string in decreasing order based on their frequency.
        
        Time complexity: O(n log n) or O(n + k log k) where k is the number of unique characters.
        Space complexity: O(n) to store the result.
        """
        count = Counter(s)
        # Sort characters by their frequency in descending order
        sorted_chars = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        res = []
        for char, freq in sorted_chars:
            res.append(char * freq)
            
        return "".join(res)
