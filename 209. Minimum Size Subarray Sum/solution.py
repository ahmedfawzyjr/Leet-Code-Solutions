from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = float('inf')
        left = 0
        current_sum = 0
        
        for right in range(n):
            current_sum += nums[right]
            
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
                
        return min_len if min_len != float('inf') else 0

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    target = 7
    nums = [2,3,1,2,4,3]
    print(f"Example 1: {sol.minSubArrayLen(target, nums)}") # Expected: 2
    
    # Example 2
    target = 4
    nums = [1,4,4]
    print(f"Example 2: {sol.minSubArrayLen(target, nums)}") # Expected: 1
    
    # Example 3
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    print(f"Example 3: {sol.minSubArrayLen(target, nums)}") # Expected: 0
