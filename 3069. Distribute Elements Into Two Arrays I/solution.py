from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        """
        Distributes all elements of nums between two arrays arr1 and arr2.
        
        Rules:
        - First operation: append nums[0] to arr1.
        - Second operation: append nums[1] to arr2.
        - For subsequent operations (nums[i] for i >= 2):
          - If the last element of arr1 > last element of arr2, append nums[i] to arr1.
          - Otherwise, append nums[i] to arr2.
        - Return the concatenation of arr1 and arr2.

        Time Complexity: O(n) where n is the length of nums.
        Space Complexity: O(n) to store arr1, arr2 and the result.
        """
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        
        for num in nums[2:]:
            if arr1[-1] > arr2[-1]:
                arr1.append(num)
            else:
                arr2.append(num)
                
        return arr1 + arr2


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    # Input: nums = [2,1,3]
    # Output: [2,3,1]
    assert sol.resultArray([2, 1, 3]) == [2, 3, 1]
    
    # Example 2
    # Input: nums = [5,4,3,8]
    # Output: [5,3,4,8]
    assert sol.resultArray([5, 4, 3, 8]) == [5, 3, 4, 8]
    
    print("All test cases passed!")
