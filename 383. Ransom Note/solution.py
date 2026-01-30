from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count characters in both strings
        ransom_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)
        
        # Check if magazine has enough characters for ransomNote
        for char, count in ransom_counts.items():
            if magazine_counts[char] < count:
                return False
        
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct("a", "b")) # Expected: False
    print(sol.canConstruct("aa", "ab")) # Expected: False
    print(sol.canConstruct("aa", "aab")) # Expected: True
