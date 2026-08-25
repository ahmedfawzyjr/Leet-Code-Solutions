from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        """
        Returns the smallest positive multiple of k that is missing from nums.

        Approach:
        1. Store all elements of `nums` in a hash set for O(1) average lookup time.
        2. Start checking positive multiples of k sequentially (k, 2k, 3k, ...).
        3. Return the first multiple that is not present in the hash set.

        Complexity:
        - Time: O(N) where N is the length of nums. Building the set takes O(N) time,
          and the loop checks at most N + 1 multiples before finding a missing one.
        - Space: O(N) to store elements in the hash set.
        """
        num_set = set(nums)
        multiple = k
        while multiple in num_set:
            multiple += k
        return multiple


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    # Input: nums = [8, 2, 3, 4, 6], k = 2
    # Output: 10
    # Explanation: Multiples of 2 are 2, 4, 6, 8, 10... Smallest missing is 10.
    res1 = sol.missingMultiple([8, 2, 3, 4, 6], 2)
    assert res1 == 10, f"Failed Example 1: expected 10, got {res1}"

    # Example 2
    # Input: nums = [1, 4, 7, 10, 15], k = 5
    # Output: 5
    # Explanation: Multiples of 5 are 5, 10, 15... Smallest missing is 5.
    res2 = sol.missingMultiple([1, 4, 7, 10, 15], 5)
    assert res2 == 5, f"Failed Example 2: expected 5, got {res2}"

    # Additional Test Cases:
    # 1. k itself is not in nums
    res3 = sol.missingMultiple([1, 2, 3], 4)
    assert res3 == 4, f"Failed Test 3: expected 4, got {res3}"

    # 2. Single element matching k
    res4 = sol.missingMultiple([2], 2)
    assert res4 == 4, f"Failed Test 4: expected 4, got {res4}"

    # 3. Multiple duplicates in nums
    res5 = sol.missingMultiple([3, 3, 6, 6, 9], 3)
    assert res5 == 12, f"Failed Test 5: expected 12, got {res5}"

    # 4. nums contains higher multiples but misses earlier ones
    res6 = sol.missingMultiple([12, 18, 24], 6)
    assert res6 == 6, f"Failed Test 6: expected 6, got {res6}"

    print("All test cases passed successfully!")
