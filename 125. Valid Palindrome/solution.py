class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        return filtered_chars == filtered_chars[::-1]

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    s1 = "A man, a plan, a canal: Panama"
    output1 = solution.isPalindrome(s1)
    print(f"Example 1: Input: s = \"{s1}\", Output: {output1}")
    assert output1 == True
    
    # Example 2
    s2 = "race a car"
    output2 = solution.isPalindrome(s2)
    print(f"Example 2: Input: s = \"{s2}\", Output: {output2}")
    assert output2 == False
    
    # Example 3
    s3 = " "
    output3 = solution.isPalindrome(s3)
    print(f"Example 3: Input: s = \"{s3}\", Output: {output3}")
    assert output3 == True

    print("All test cases passed!")
