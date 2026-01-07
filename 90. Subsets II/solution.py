from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def backtrack(start, subset):
            res.append(subset[:])
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        
        backtrack(0, [])
        return res

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [1, 2, 2]
    print(f"Input: nums = {nums1}")
    print(f"Output: {sol.subsetsWithDup(nums1)}")
    
    # Example 2
    nums2 = [0]
    print(f"Input: nums = {nums2}")
    print(f"Output: {sol.subsetsWithDup(nums2)}")
