class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        """
        A letter is special if it appears both in lowercase and uppercase, 
        and every lowercase occurrence appears before the first uppercase occurrence.
        
        Complexity:
        - Time: O(N) where N is the length of the word.
        - Space: O(1) to store indices for 26 letters.
        """
        # last_lower stores the last seen index of each lowercase letter
        last_lower = {}
        # first_upper stores the first seen index of each uppercase letter
        first_upper = {}
        
        for i, char in enumerate(word):
            if 'a' <= char <= 'z':
                last_lower[char] = i
            elif 'A' <= char <= 'Z':
                if char not in first_upper:
                    first_upper[char] = i
        
        count = 0
        for i in range(26):
            lower = chr(ord('a') + i)
            upper = chr(ord('A') + i)
            
            if lower in last_lower and upper in first_upper:
                if last_lower[lower] < first_upper[upper]:
                    count += 1
                    
        return count
