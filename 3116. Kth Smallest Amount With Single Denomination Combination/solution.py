import math
from typing import List


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        """
        Finds the kth smallest amount that can be made using an infinite number
        of coins of each single denomination combination (no combinations of different coins).

        Approach:
        1. Redundancy Pruning:
           - Sort coins in ascending order.
           - If a coin is a multiple of any smaller coin in the list, it adds no new
             multiples and can be pruned.
        2. Principle of Inclusion-Exclusion (PIE):
           - Precompute all non-empty subsets of pruned coins.
           - For each subset, calculate LCM of the subset.
           - Assign sign +1 for odd subset sizes and -1 for even subset sizes.
        3. Binary Search on Answer:
           - Range: [1, min(coins) * k]
           - For a candidate value X, the count of valid amounts <= X is:
             Count(X) = sum(sign * (X // LCM(subset)))
           - Find the smallest X such that Count(X) >= k.

        Time Complexity: O(2^n * log(min(coins) * k)), where n <= 15 is the number of pruned coins.
        Space Complexity: O(2^n) to store the subset LCMs and signs.
        """
        # Step 1: Filter out redundant coins (multiples of smaller coins)
        coins = sorted(coins)
        pruned = []
        for c in coins:
            if not any(c % p == 0 for p in pruned):
                pruned.append(c)
        coins = pruned

        n = len(coins)
        subsets = []

        # Step 2: Precompute LCM and sign for all non-empty subsets
        for mask in range(1, 1 << n):
            cur_lcm = 1
            bits_count = 0
            for i in range(n):
                if (mask >> i) & 1:
                    bits_count += 1
                    cur_lcm = math.lcm(cur_lcm, coins[i])
            sign = 1 if bits_count % 2 == 1 else -1
            subsets.append((cur_lcm, sign))

        # Helper to calculate how many values <= x are multiples of at least one coin
        def count_multiples_le(x: int) -> int:
            cnt = 0
            for lcm_val, sign in subsets:
                cnt += sign * (x // lcm_val)
            return cnt

        # Step 3: Binary search on the answer
        left = 1
        right = min(coins) * k
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if count_multiples_le(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    # Input: coins = [3,6,9], k = 3
    # Output: 9
    assert sol.findKthSmallest([3, 6, 9], 3) == 9

    # Example 2
    # Input: coins = [5,2], k = 7
    # Output: 12
    assert sol.findKthSmallest([5, 2], 7) == 12

    # Additional Test Cases
    # Single coin
    assert sol.findKthSmallest([1], 100) == 100
    assert sol.findKthSmallest([5], 10) == 50

    # Pruned multiple coins
    assert sol.findKthSmallest([2, 4, 8, 16], 5) == 10

    # Maximum k with multiple prime coins
    assert sol.findKthSmallest([13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], 2000000000) == 4369625464

    print("All test cases passed!")
