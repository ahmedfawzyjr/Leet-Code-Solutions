class Solution:
    def sumGame(self, num: str) -> bool:
        """
        Determines whether Alice will win the Sum Game.

        Game Rules & Strategy:
        - num has even length n.
        - Alice moves first; Bob moves second.
        - Alice wants the sum of the first half != sum of the second half.
        - Bob wants the sum of the first half == sum of the second half.

        Analysis:
        1. If the total number of '?' (c1 + c2) is odd:
           - Alice makes the final move.
           - Right before the last move, exactly one '?' remains.
           - There is at most one digit out of [0..9] that makes the sums equal.
           - Alice can always pick any other digit to force inequality. Alice wins (True).

        2. If the total number of '?' (c1 + c2) is even:
           - Bob makes the final move.
           - For the min(c1, c2) '?' on each side, Bob mirrors Alice's plays on the opposing side.
           - For the |c1 - c2| excess '?' on the side with more '?', there are |c1 - c2| / 2 pairs of turns.
           - On each pair, Bob can pair Alice's choice d with (9 - d), ensuring each pair contributes 9.
           - Thus, Bob can only neutralize a deficit of ((c2 - c1) / 2) * 9 on the right (or vice-versa).
           - If (s1 - s2) == ((c2 - c1) / 2) * 9, Bob can guarantee equality. Bob wins (False).
           - Otherwise, Alice can exploit the discrepancy to win (True).

        Unified Condition:
        Alice wins iff:
            2 * (s1 - s2) != 9 * (c2 - c1)

        Complexity:
        - Time: O(n) - Single pass over the string of length n.
        - Space: O(1) - Constant auxiliary space for sum and count accumulators.
        """
        n = len(num)
        half = n // 2
        
        s1 = 0
        c1 = 0
        for i in range(half):
            if num[i] == '?':
                c1 += 1
            else:
                s1 += int(num[i])
                
        s2 = 0
        c2 = 0
        for i in range(half, n):
            if num[i] == '?':
                c2 += 1
            else:
                s2 += int(num[i])
                
        return 2 * (s1 - s2) != 9 * (c2 - c1)


if __name__ == "__main__":
    sol = Solution()

    # Example 1: num = "5023" -> False
    # Left sum = 5, Right sum = 5, no '?' -> sums equal -> Bob wins
    assert sol.sumGame("5023") is False, "Failed on Example 1: '5023'"

    # Example 2: num = "25??" -> True
    # Left sum = 7, c1 = 0, Right sum = 0, c2 = 2. 2 * (7 - 0) = 14 != 9 * (2 - 0) = 18 -> Alice wins
    assert sol.sumGame("25??") is True, "Failed on Example 2: '25??'"

    # Example 3: num = "?3295???" -> False
    # Left sum = 14, c1 = 1, Right sum = 5, c2 = 3. 2 * (14 - 5) = 18 == 9 * (3 - 1) = 18 -> Bob wins
    assert sol.sumGame("?3295???") is False, "Failed on Example 3: '?3295???'"

    # Additional Test Cases:
    # Odd number of '?' -> Alice always wins
    assert sol.sumGame("?2") is True, "Failed on single '?'"
    assert sol.sumGame("?3295??0") is True, "Failed on odd total '?'"

    # Symmetrical question marks with equal known sums -> Bob wins
    assert sol.sumGame("??") is False, "Failed on '??'"
    assert sol.sumGame("????") is False, "Failed on '????'"
    assert sol.sumGame("1?1?") is False, "Failed on '1?1?'"
    
    # Symmetrical question marks with unequal sums -> Alice wins
    assert sol.sumGame("1?2?") is True, "Failed on '1?2?'"
    assert sol.sumGame("9???") is True, "Failed on '9???'"

    print("All test cases passed successfully!")
