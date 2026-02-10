from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        for i in range(n):
            # If the remaining elements are not enough to beat the current max_len, stop.
            if n - i <= max_len:
                break
            
            evens = set()
            odds = set()
            for j in range(i, n):
                val = nums[j]
                if val % 2 == 0:
                    evens.add(val)
                else:
                    odds.add(val)
                
                if len(evens) == len(odds):
                    length = j - i + 1
                    if length > max_len:
                        max_len = length
        
        return max_len
