from typing import List
import math

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        # Bucket Sort approach for O(N) time and space
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
            
        n = len(nums)
        bucket_size = math.ceil((max_val - min_val) / (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]
        
        for num in nums:
            idx = (num - min_val) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)
            
        max_gap = 0
        prev_max = min_val
        
        for i in range(bucket_count):
            if buckets[i][0] == float('inf'):
                continue
                
            max_gap = max(max_gap, buckets[i][0] - prev_max)
            prev_max = buckets[i][1]
            
        return max_gap

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    nums1 = [3,6,9,1]
    print(f"Input: {nums1}")
    print(f"Output: {solution.maximumGap(nums1)}")
    # Expected: 3
    
    # Example 2
    nums2 = [10]
    print(f"Input: {nums2}")
    print(f"Output: {solution.maximumGap(nums2)}")
    # Expected: 0
