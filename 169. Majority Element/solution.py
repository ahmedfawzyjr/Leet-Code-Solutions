from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
            
        return candidate

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [3,2,3]
    print(f"Example 1 Output: {sol.majorityElement(nums1)}") # Expected: 3
    
    # Example 2
    nums2 = [2,2,1,1,1,2,2]
    print(f"Example 2 Output: {sol.majorityElement(nums2)}") # Expected: 2
