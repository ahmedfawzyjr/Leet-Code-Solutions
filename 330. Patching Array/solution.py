from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        reach = 0
        i = 0
        
        while reach < n:
            if i < len(nums) and nums[i] <= reach + 1:
                reach += nums[i]
                i += 1
            else:
                reach += reach + 1
                patches += 1
                
        return patches

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [1, 3]
    n1 = 6
    print(f"Example 1: {sol.minPatches(nums1, n1)}") # Expected: 1
    
    # Example 2
    nums2 = [1, 5, 10]
    n2 = 20
    print(f"Example 2: {sol.minPatches(nums2, n2)}") # Expected: 2
    
    # Example 3
    nums3 = [1, 2, 2]
    n3 = 5
    print(f"Example 3: {sol.minPatches(nums3, n3)}") # Expected: 0
