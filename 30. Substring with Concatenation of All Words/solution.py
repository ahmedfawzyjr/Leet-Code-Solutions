from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Find all starting indices of substring(s) in s that is a 
        concatenation of each word in words exactly once.
        
        Uses sliding window with word frequency counting.
        
        Time Complexity: O(n * m * word_len) where n = len(s), m = len(words)
        Space Complexity: O(m) for the frequency maps
        """
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        result = []
        
        # Try each starting position within word_len
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            
            while right + word_len <= len(s):
                # Get the word at current position
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    current_count[word] += 1
                    
                    # Shrink window if we have too many of this word
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len
                    
                    # Check if we have a valid concatenation
                    if right - left == total_len:
                        result.append(left)
                else:
                    # Reset the window
                    current_count.clear()
                    left = right
        
        return result
