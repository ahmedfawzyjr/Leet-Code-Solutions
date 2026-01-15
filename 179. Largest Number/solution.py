from typing import List
import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert integers to strings
        nums_str = [str(num) for num in nums]
        
        # Custom comparator
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        # Sort using the custom comparator
        nums_str.sort(key=functools.cmp_to_key(compare))
        
        # Join the sorted strings
        largest_num = ''.join(nums_str)
        
        # Handle the case where the result is "00...0"
        return "0" if largest_num[0] == "0" else largest_num

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [10, 2]
    print(f"Example 1 Output: {sol.largestNumber(nums1)}") # Expected: "210"
    
    # Example 2
    nums2 = [3, 30, 34, 5, 9]
    print(f"Example 2 Output: {sol.largestNumber(nums2)}") # Expected: "9534330"
