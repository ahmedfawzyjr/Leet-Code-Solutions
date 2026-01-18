from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        def rob_linear(houses):
            if not houses:
                return 0
            if len(houses) == 1:
                return houses[0]
            
            prev2 = 0
            prev1 = 0
            
            for money in houses:
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current
                
            return prev1
            
        # Case 1: Rob houses 0 to n-2 (exclude last)
        max1 = rob_linear(nums[:-1])
        
        # Case 2: Rob houses 1 to n-1 (exclude first)
        max2 = rob_linear(nums[1:])
        
        return max(max1, max2)

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums = [2,3,2]
    print(f"Example 1: {sol.rob(nums)}") # Expected: 3
    
    # Example 2
    nums = [1,2,3,1]
    print(f"Example 2: {sol.rob(nums)}") # Expected: 4
    
    # Example 3
    nums = [1,2,3]
    print(f"Example 3: {sol.rob(nums)}") # Expected: 3
