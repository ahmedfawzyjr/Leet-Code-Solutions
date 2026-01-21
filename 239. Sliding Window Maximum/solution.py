from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
        You can only see the k numbers in the window. Each time the sliding window moves right by one position.
        Return the max sliding window.
        """
        if not nums:
            return []
        
        result = []
        window = deque()  # Stores indices
        
        for i, num in enumerate(nums):
            # Remove indices that are out of the current window
            while window and window[0] < i - k + 1:
                window.popleft()
            
            # Remove indices whose corresponding values are less than the current num
            while window and nums[window[-1]] < num:
                window.pop()
            
            window.append(i)
            
            # Add the maximum element of the current window to the result
            if i >= k - 1:
                result.append(nums[window[0]])
                
        return result

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = sol.maxSlidingWindow(nums, k)
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Output: {result} (Expected: [3, 3, 5, 5, 6, 7])")
    
    # Test Case 2
    nums = [1]
    k = 1
    result = sol.maxSlidingWindow(nums, k)
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Output: {result} (Expected: [1])")
