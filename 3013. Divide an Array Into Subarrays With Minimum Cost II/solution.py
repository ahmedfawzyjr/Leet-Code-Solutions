from typing import List
import heapq
from collections import Counter

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        target_k = k - 1
        
        low = [] # max-heap
        high = [] # min-heap
        to_delete = Counter()
        sum_low = 0
        count_low = 0
        count_high = 0
        
        def clean_low():
            while low and to_delete[-low[0]] > 0:
                to_delete[-heapq.heappop(low)] -= 1
                
        def clean_high():
            while high and to_delete[high[0]] > 0:
                to_delete[heapq.heappop(high)] -= 1
                
        def balance():
            nonlocal sum_low, count_low, count_high
            # Lower to higher
            while count_low > target_k:
                clean_low()
                val = -heapq.heappop(low)
                sum_low -= val
                count_low -= 1
                heapq.heappush(high, val)
                count_high += 1
            
            # Higher to lower
            while count_low < target_k and count_high > 0:
                clean_high()
                val = heapq.heappop(high)
                sum_low += val
                count_low += 1
                count_high -= 1
                heapq.heappush(low, -val)
            
            clean_low()
            clean_high()

        def add(val):
            nonlocal sum_low, count_low, count_high
            clean_low()
            if not low or val <= -low[0]:
                heapq.heappush(low, -val)
                sum_low += val
                count_low += 1
            else:
                heapq.heappush(high, val)
                count_high += 1
            balance()
            
        def remove(val):
            nonlocal sum_low, count_low, count_high
            clean_low()
            if val <= -low[0]:
                sum_low -= val
                count_low -= 1
            else:
                count_high -= 1
            to_delete[val] += 1
            balance()

        # Initialize first window [1, dist+1]
        for i in range(1, dist + 2):
            add(nums[i])
            
        min_cost = sum_low
        
        # Slide window
        # Window starts at j, ends at j + dist.
        # Initial j=1, ends at 1+dist.
        # Next j=2, ends at 2+dist.
        # Max j + dist = n - 1 => j = n - 1 - dist.
        for j in range(2, n - dist):
            remove(nums[j-1])
            add(nums[j + dist])
            min_cost = min(min_cost, sum_low)
            
        return nums[0] + min_cost
