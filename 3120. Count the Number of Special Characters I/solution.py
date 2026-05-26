class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        """
        A letter is called special if it appears both in lowercase and uppercase in word.
        
        Complexity:
        - Time: O(N) where N is the length of the word.
        - Space: O(1) as the number of English letters is constant (52 max in sets).
        """
        chars = set(word)
        count = 0
        
        # Check each lowercase letter from 'a' to 'z'
        for i in range(26):
            lower = chr(ord('a') + i)
            upper = chr(ord('A') + i)
            if lower in chars and upper in chars:
                count += 1
                
        return count
