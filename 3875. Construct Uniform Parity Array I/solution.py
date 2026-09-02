from typing import List


class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        """
        Determines whether it is possible to construct an array nums2 of length n
        such that all elements in nums2 are either all odd or all even.

        Mathematical Parity Analysis:
        - Target Parity: All EVEN
          - If nums1[i] is even, choose nums2[i] = nums1[i] (even).
          - If nums1[i] is odd, choose nums2[i] = nums1[i] - nums1[j] with odd nums1[j] (j != i).
            odd - odd = even. This is possible if count(odd) >= 2.
          - Thus, an all-even nums2 is possible if count(odd) == 0 or count(odd) >= 2 (i.e. count(odd) != 1).

        - Target Parity: All ODD
          - If nums1[i] is odd, choose nums2[i] = nums1[i] (odd).
          - If nums1[i] is even, choose nums2[i] = nums1[i] - nums1[j] with odd nums1[j] (j != i).
            even - odd = odd. This is possible if count(odd) >= 1.
          - Thus, an all-odd nums2 is possible if count(odd) >= 1.

        - Overall Feasibility:
          - If count(odd) == 0 -> All-even is achievable (True).
          - If count(odd) == 1 -> All-odd is achievable (True).
          - If count(odd) >= 2 -> Both all-even and all-odd are achievable (True).
          - For n = 1, nums2[0] = nums1[0] is trivially uniform in parity (True).

        Therefore, it is unconditionally possible to construct a uniform parity array for any input.

        Complexity:
        - Time Complexity: O(1)
        - Space Complexity: O(1)
        """
        return True


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    # Input: nums1 = [2, 3]
    # Output: true
    # Explanation: nums2[0] = 2 - 3 = -1 (odd), nums2[1] = 3 (odd) -> all odd.
    assert sol.uniformArray([2, 3]) is True, "Failed Example 1"

    # Example 2
    # Input: nums1 = [4, 6]
    # Output: true
    # Explanation: nums2[0] = 4 (even), nums2[1] = 6 (even) -> all even.
    assert sol.uniformArray([4, 6]) is True, "Failed Example 2"

    # Additional Test Cases:
    # All odd
    assert sol.uniformArray([1, 3, 5]) is True
    # Single element
    assert sol.uniformArray([7]) is True
    assert sol.uniformArray([8]) is True
    # Exactly one odd with multiple evens
    assert sol.uniformArray([2, 4, 1, 6]) is True
    # Exactly two odds with multiple evens
    assert sol.uniformArray([2, 4, 1, 3, 6]) is True
    # Mixed values up to 100
    assert sol.uniformArray(list(range(1, 101))) is True

    print("All test cases passed successfully!")
