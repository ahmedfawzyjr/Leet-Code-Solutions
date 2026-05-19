from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
                
        return -1

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    nums1_1 = [1, 2, 3]
    nums2_1 = [2, 4]
    print(f"Input: nums1 = {nums1_1}, nums2 = {nums2_1}")
    print(f"Output: {solution.getCommon(nums1_1, nums2_1)}")
    # Expected: 2
    
    # Example 2
    nums1_2 = [1, 2, 3, 6]
    nums2_2 = [2, 3, 4, 5]
    print(f"Input: nums1 = {nums1_2}, nums2 = {nums2_2}")
    print(f"Output: {solution.getCommon(nums1_2, nums2_2)}")
    # Expected: 2
