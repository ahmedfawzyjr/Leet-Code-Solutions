from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Calculate how much water can be trapped after raining.
        
        Two-pointer approach: Water at any position = min(left_max, right_max) - height[i]
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        
        while left < right:
            if left_max < right_max:
                # Water level is determined by left_max
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                # Water level is determined by right_max
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        
        return water
    
    def trap_dp(self, height: List[int]) -> int:
        """
        Alternative: Dynamic Programming approach
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not height:
            return 0
        
        n = len(height)
        
        # left_max[i] = max height from index 0 to i
        left_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        
        # right_max[i] = max height from index i to n-1
        right_max = [0] * n
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        # Calculate water at each position
        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]
        
        return water


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: height = [0,1,0,2,1,0,1,3,2,1,2,1] -> Output: 6
    print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    
    # Example 2: height = [4,2,0,3,2,5] -> Output: 9
    print(sol.trap([4, 2, 0, 3, 2, 5]))  # 9
