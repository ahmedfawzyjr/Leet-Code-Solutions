from typing import List

class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        n = len(x)
        if n <= 3:
            return False
            
        for i in range(3, n):
            # Case 1: Fourth line crosses first line
            if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
                return True
            
            # Case 2: Fifth line meets first line
            if i >= 4:
                if x[i-1] == x[i-3] and x[i] + x[i-4] >= x[i-2]:
                    return True
            
            # Case 3: Sixth line crosses first line
            if i >= 5:
                if x[i-2] >= x[i-4] and x[i] + x[i-4] >= x[i-2] and \
                   x[i-1] <= x[i-3] and x[i-1] + x[i-5] >= x[i-3]:
                    return True
                    
        return False

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    distance1 = [2, 1, 1, 2]
    print(f"Example 1: {sol.isSelfCrossing(distance1)}") # Expected: True
    
    # Example 2
    distance2 = [1, 2, 3, 4]
    print(f"Example 2: {sol.isSelfCrossing(distance2)}") # Expected: False
    
    # Example 3
    distance3 = [1, 1, 1, 2, 1]
    print(f"Example 3: {sol.isSelfCrossing(distance3)}") # Expected: True
