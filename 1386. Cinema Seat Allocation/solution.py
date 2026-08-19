from typing import List
from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        """
        Calculates the maximum number of 4-person family groups that can be seated.
        
        A 4-person group can be seated in:
        - Left block: seats [2, 3, 4, 5]
        - Middle block: seats [4, 5, 6, 7]
        - Right block: seats [6, 7, 8, 9]
        
        Seats 1 and 10 do not affect any 4-person group.
        
        Strategy:
        - Any row with no reservations in seats [2..9] can fit 2 groups (Left + Right).
        - For rows that have reservations in seats [2..9], we use a bitmask to check:
          1. If both Left and Right blocks are available -> +2 groups
          2. Else if either Left or Right block is available -> +1 group
          3. Else if Middle block is available -> +1 group
        
        Time Complexity: O(M), where M is the number of reserved seats.
        Space Complexity: O(M), to store reserved seats per row.
        """
        # Bitmasks for seats 2-9 (1-indexed)
        LEFT_MASK = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)    # 0b0000111100 = 60
        RIGHT_MASK = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)   # 0b1111000000 = 960
        MID_MASK = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)     # 0b0011110000 = 240
        
        reserved_mask = defaultdict(int)
        
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                reserved_mask[row] |= (1 << col)
        
        # Rows with no reservations in seats 2..9 can seat 2 groups each
        total_groups = (n - len(reserved_mask)) * 2
        
        for mask in reserved_mask.values():
            left_available = (mask & LEFT_MASK) == 0
            right_available = (mask & RIGHT_MASK) == 0
            
            if left_available and right_available:
                total_groups += 2
            elif left_available or right_available:
                total_groups += 1
            elif (mask & MID_MASK) == 0:
                total_groups += 1
                
        return total_groups


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    # Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
    # Output: 4
    print("Example 1:", sol.maxNumberOfFamilies(3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]))
    assert sol.maxNumberOfFamilies(3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]) == 4
    
    # Example 2
    # Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
    # Output: 2
    print("Example 2:", sol.maxNumberOfFamilies(2, [[2,1],[1,8],[2,6]]))
    assert sol.maxNumberOfFamilies(2, [[2,1],[1,8],[2,6]]) == 2
    
    # Example 3
    # Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
    # Output: 4
    print("Example 3:", sol.maxNumberOfFamilies(4, [[4,3],[1,4],[4,6],[1,7]]))
    assert sol.maxNumberOfFamilies(4, [[4,3],[1,4],[4,6],[1,7]]) == 4
    
    print("All test cases passed!")
