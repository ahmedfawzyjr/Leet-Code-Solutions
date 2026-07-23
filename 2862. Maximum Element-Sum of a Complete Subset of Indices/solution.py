class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        # A complete subset of indices is a set of 1-based indices where every pair's product is a perfect square.
        # Two indices i and j have i * j = perfect square if and only if i and j share the exact same square-free core (base).
        # Any index i can be represented as c * k^2 where c is a square-free integer and k >= 1.
        # Thus, all indices with the same base c form a complete subset: c * 1^2, c * 2^2, c * 3^2, ...
        # Since nums[i] >= 1, the maximum sum for a base c is obtained by summing nums[c * k^2 - 1] for all valid k.
        # Checking all c from 1 to n encompasses all square-free bases (non-square-free c will produce a subset of a square-free base).

        n = len(nums)
        max_sum = 0

        for c in range(1, n + 1):
            current_sum = 0
            k = 1
            idx = c * k * k
            while idx <= n:
                current_sum += nums[idx - 1]
                k += 1
                idx = c * k * k
            
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum
