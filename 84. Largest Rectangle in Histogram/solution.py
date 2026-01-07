from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        for i, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)
            
        return max_area

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    heights1 = [2, 1, 5, 6, 2, 3]
    print(f"Input: heights = {heights1}")
    print(f"Output: {sol.largestRectangleArea(heights1)}")
    
    # Example 2
    heights2 = [2, 4]
    print(f"Input: heights = {heights2}")
    print(f"Output: {sol.largestRectangleArea(heights2)}")
