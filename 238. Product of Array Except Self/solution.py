from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        You must write an algorithm that runs in O(n) time and without using the division operation.
        """
        n = len(nums)
        answer = [1] * n
        
        # Calculate left products
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
            
        # Calculate right products and update answer
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
            
        return answer

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    nums = [1, 2, 3, 4]
    result = sol.productExceptSelf(nums)
    print(f"Input: {nums}")
    print(f"Output: {result} (Expected: [24, 12, 8, 6])")
    
    # Test Case 2
    nums = [-1, 1, 0, -3, 3]
    result = sol.productExceptSelf(nums)
    print(f"Input: {nums}")
    print(f"Output: {result} (Expected: [0, 0, 9, 0, 0])")
