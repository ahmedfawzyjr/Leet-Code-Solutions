from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            idx = bisect.bisect_left(tails, num)
            if idx < len(tails):
                tails[idx] = num
            else:
                tails.append(num)
        return len(tails)
