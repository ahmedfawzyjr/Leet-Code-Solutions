import bisect
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = sorted(nums[:k])
        res = []
        
        def get_median(window, k):
            if k % 2 == 1:
                return float(window[k // 2])
            else:
                return (window[k // 2 - 1] + window[k // 2]) / 2.0
        
        res.append(get_median(window, k))
        
        for i in range(k, len(nums)):
            # Remove the element that is out of the window
            # Use bisect_left to find the index of the element to remove
            idx = bisect.bisect_left(window, nums[i - k])
            window.pop(idx)
            
            # Insert the new element
            bisect.insort(window, nums[i])
            
            res.append(get_median(window, k))
            
        return res
