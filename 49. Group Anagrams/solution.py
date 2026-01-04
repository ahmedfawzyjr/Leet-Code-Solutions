from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams together using sorted string as key.
        
        Anagrams have the same sorted characters, so we use that as a hash key.
        
        Time Complexity: O(n * k log k) where n = len(strs), k = max string length
        Space Complexity: O(n * k)
        """
        anagram_groups = defaultdict(list)
        
        for s in strs:
            # Sort the string to create a canonical key
            key = ''.join(sorted(s))
            anagram_groups[key].append(s)
        
        return list(anagram_groups.values())
    
    def groupAnagrams_count(self, strs: List[str]) -> List[List[str]]:
        """
        Alternative: Use character count as key (faster for long strings).
        
        Time Complexity: O(n * k) where n = len(strs), k = max string length
        Space Complexity: O(n * k)
        """
        anagram_groups = defaultdict(list)
        
        for s in strs:
            # Create a count array for 26 letters
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Use tuple of counts as key (tuples are hashable)
            key = tuple(count)
            anagram_groups[key].append(s)
        
        return list(anagram_groups.values())


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: strs = ["eat","tea","tan","ate","nat","bat"]
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [["bat"],["nat","tan"],["ate","eat","tea"]]
    
    # Example 2: strs = [""]
    print(sol.groupAnagrams([""]))  # [[""]]
    
    # Example 3: strs = ["a"]
    print(sol.groupAnagrams(["a"]))  # [["a"]]
