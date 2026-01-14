class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string by whitespace and filter out empty strings
        words = s.split()
        # Reverse the list of words
        words.reverse()
        # Join the words with a single space
        return " ".join(words)

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    s1 = "the sky is blue"
    print(f"Input: '{s1}'")
    print(f"Output: '{solution.reverseWords(s1)}'")
    # Expected: "blue is sky the"
    
    # Example 2
    s2 = "  hello world  "
    print(f"Input: '{s2}'")
    print(f"Output: '{solution.reverseWords(s2)}'")
    # Expected: "world hello"
    
    # Example 3
    s3 = "a good   example"
    print(f"Input: '{s3}'")
    print(f"Output: '{solution.reverseWords(s3)}'")
    # Expected: "example good a"
