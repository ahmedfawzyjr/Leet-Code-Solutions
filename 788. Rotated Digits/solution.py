class Solution:
    def rotatedDigits(self, n: int) -> int:
        """
        An integer x is good if after rotating each digit individually by 180 degrees, 
        it results in a valid number that is different from x.
        
        Rotation rules:
        - 0, 1, 8: Rotate to themselves (stay valid, same value)
        - 2, 5: Rotate to each other (stay valid, different value)
        - 6, 9: Rotate to each other (stay valid, different value)
        - 3, 4, 7: Invalid after rotation
        
        A number is "good" if:
        1. It contains ONLY digits from {0, 1, 8, 2, 5, 6, 9}.
        2. It contains AT LEAST ONE digit from {2, 5, 6, 9} (to ensure the rotated number is different).
        """
        count = 0
        for i in range(1, n + 1):
            s = str(i)
            # Check for invalid digits
            if any(c in '347' for c in s):
                continue
            # Check if it's different after rotation
            if any(c in '2569' for c in s):
                count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    # Test cases from LeetCode
    assert sol.rotatedDigits(10) == 4   # 2, 5, 6, 9 are good
    assert sol.rotatedDigits(1) == 0
    assert sol.rotatedDigits(2) == 1    # 2 is good
    print("All tests passed!")
