class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        """
        Determines if string halves 'a' and 'b' have the same number of vowels.

        Approach:
        1. Create a set of vowels containing both lowercase and uppercase vowels.
        2. Calculate the midpoint `mid = len(s) // 2`.
        3. Iterate through index 0 to mid - 1, incrementing balance for vowels in
           the first half and decrementing balance for vowels in the second half.
        4. Return True if balance equals 0, else False.

        Complexity:
        - Time Complexity: O(n), where n is the length of string s.
        - Space Complexity: O(1) auxiliary space.
        """
        vowels = set("aeiouAEIOU")
        mid = len(s) // 2
        balance = 0

        for i in range(mid):
            if s[i] in vowels:
                balance += 1
            if s[mid + i] in vowels:
                balance -= 1

        return balance == 0


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    # Input: s = "book" -> a = "bo" (1 vowel), b = "ok" (1 vowel) -> True
    assert sol.halvesAreAlike("book") is True, "Failed Example 1"

    # Example 2
    # Input: s = "textbook" -> a = "text" (1 vowel), b = "book" (2 vowels) -> False
    assert sol.halvesAreAlike("textbook") is False, "Failed Example 2"

    # Additional Test Cases
    # Case with uppercase vowels
    assert sol.halvesAreAlike("AbCdEfGh") is True  # a="AbCd" (A), b="EfGh" (E) -> 1 and 1
    assert sol.halvesAreAlike("AbCdEfGH") is True
    assert sol.halvesAreAlike("UuUu") is True  # a="Uu" (2), b="Uu" (2)
    assert sol.halvesAreAlike("UuAa") is True
    assert sol.halvesAreAlike("bcdfgk") is True  # 0 vowels on both sides
    assert sol.halvesAreAlike("aA") is True

    print("All test cases passed successfully!")
