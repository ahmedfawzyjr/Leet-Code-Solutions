from collections import defaultdict
from typing import List

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # Group suffixes by their first character
        suffixes = defaultdict(set)
        for idea in ideas:
            suffixes[idea[0]].add(idea[1:])
        
        keys = list(suffixes.keys())
        n = len(keys)
        ans = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                char1, char2 = keys[i], keys[j]
                set1, set2 = suffixes[char1], suffixes[char2]
                
                # Find size of intersection
                intersect_count = len(set1 & set2)
                
                # Valid words starting with char1 that can pair with valid words starting with char2
                valid1 = len(set1) - intersect_count
                valid2 = len(set2) - intersect_count
                
                # Each valid pair can form 2 distinct company names (ideaA ideaB and ideaB ideaA)
                ans += 2 * valid1 * valid2
                
        return ans
