from typing import List
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        Returns the number of good pairs (i, j) such that nums[i] == nums[j] and i < j.

        Approach:
        1. Single-Pass Hash Map (Counting On the Fly):
           - As we iterate through `nums`, each previous occurrence of `num` can pair with
             the current index to form a valid good pair.
           - We add `count[num]` to our running total of good pairs, then increment `count[num]`.
        2. Mathematical Combinations:
           - Alternatively, count frequencies of each number. For a number appearing `k` times,
             it contributes k * (k - 1) // 2 pairs.

        Complexity:
        - Time Complexity: O(N), where N is the length of `nums`. We iterate through the array once.
        - Space Complexity: O(U), where U is the number of unique elements in `nums` (U <= min(N, 100)).
        """
        count = Counter()
        good_pairs = 0

        for num in nums:
            good_pairs += count[num]
            count[num] += 1

        return good_pairs


if __name__ == "__main__":
    sol = Solution()

    # Example 1:
    # Input: nums = [1, 2, 3, 1, 1, 3]
    # Output: 4
    # Explanation: There are 4 good pairs: (0,3), (0,4), (3,4), (2,5)
    res1 = sol.numIdenticalPairs([1, 2, 3, 1, 1, 3])
    assert res1 == 4, f"Failed Example 1: expected 4, got {res1}"

    # Example 2:
    # Input: nums = [1, 1, 1, 1]
    # Output: 6
    # Explanation: Each pair in the array is good (4 * 3 / 2 = 6).
    res2 = sol.numIdenticalPairs([1, 1, 1, 1])
    assert res2 == 6, f"Failed Example 2: expected 6, got {res2}"

    # Example 3:
    # Input: nums = [1, 2, 3]
    # Output: 0
    # Explanation: No identical elements.
    res3 = sol.numIdenticalPairs([1, 2, 3])
    assert res3 == 0, f"Failed Example 3: expected 0, got {res3}"

    # Additional Test Cases:
    # 1. Single element (minimum constraint)
    res4 = sol.numIdenticalPairs([5])
    assert res4 == 0, f"Failed Test 4: expected 0, got {res4}"

    # 2. Two identical elements
    res5 = sol.numIdenticalPairs([10, 10])
    assert res5 == 1, f"Failed Test 5: expected 1, got {res5}"

    # 3. Two pairs of distinct numbers
    res6 = sol.numIdenticalPairs([1, 2, 1, 2])
    assert res6 == 2, f"Failed Test 6: expected 2, got {res6}"

    # 4. Large frequency
    res7 = sol.numIdenticalPairs([1] * 100)
    assert res7 == 100 * 99 // 2, f"Failed Test 7: expected {100 * 99 // 2}, got {res7}"

    print("All test cases passed successfully!")
