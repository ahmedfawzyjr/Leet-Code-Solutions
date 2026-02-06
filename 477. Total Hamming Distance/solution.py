from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for i in range(32):
            count1 = 0
            for num in nums:
                count1 += (num >> i) & 1
            total += count1 * (n - count1)
        return total
