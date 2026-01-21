class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.
        """
        if len(s) != len(t):
            return False
        
        count = {}
        
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
            
        return True

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    s = "anagram"
    t = "nagaram"
    result = sol.isAnagram(s, t)
    print(f"s: {s}, t: {t}, Is Anagram: {result} (Expected: True)")
    
    # Test Case 2
    s = "rat"
    t = "car"
    result = sol.isAnagram(s, t)
    print(f"s: {s}, t: {t}, Is Anagram: {result} (Expected: False)")
