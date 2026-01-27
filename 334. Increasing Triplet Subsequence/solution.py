from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
                
        return False

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [1, 2, 3, 4, 5]
    print(f"Example 1: {sol.increasingTriplet(nums1)}") # Expected: True
    
    # Example 2
    nums2 = [5, 4, 3, 2, 1]
    print(f"Example 2: {sol.increasingTriplet(nums2)}") # Expected: False
    
    # Example 3
    nums3 = [2, 1, 5, 0, 4, 6]
    print(f"Example 3: {sol.increasingTriplet(nums3)}") # Expected: True
