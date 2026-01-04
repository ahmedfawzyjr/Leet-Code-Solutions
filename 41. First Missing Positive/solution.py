from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Find the smallest missing positive integer in O(n) time and O(1) space.
        
        Key insight: The answer must be in range [1, n+1] where n = len(nums).
        Use the array itself as a hash map by placing each number at its correct index.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(nums)
        
        # Step 1: Place each number in its correct position
        # Number 'x' should be at index 'x-1' (if 1 <= x <= n)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # Step 2: Find the first position where nums[i] != i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all positions are correct, the answer is n + 1
        return n + 1


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: nums = [1,2,0] -> Output: 3
    print(sol.firstMissingPositive([1, 2, 0]))  # 3
    
    # Example 2: nums = [3,4,-1,1] -> Output: 2
    print(sol.firstMissingPositive([3, 4, -1, 1]))  # 2
    
    # Example 3: nums = [7,8,9,11,12] -> Output: 1
    print(sol.firstMissingPositive([7, 8, 9, 11, 12]))  # 1
