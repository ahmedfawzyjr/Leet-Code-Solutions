from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Return the minimum number of jumps to reach the last index.
        
        Greedy approach: At each step, find the farthest we can reach and jump there.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_end = 0  # End of current jump range
        farthest = 0     # Farthest we can reach
        
        for i in range(n - 1):
            # Update the farthest we can reach from current position
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the end of current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Early termination if we can already reach the end
                if current_end >= n - 1:
                    break
        
        return jumps
    
    def jump_bfs(self, nums: List[int]) -> int:
        """
        Alternative: BFS approach - treat each reachable range as a level.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_level_end = 0
        next_level_end = 0
        
        i = 0
        while current_level_end < n - 1:
            jumps += 1
            # Explore all positions in current level
            while i <= current_level_end:
                next_level_end = max(next_level_end, i + nums[i])
                i += 1
            current_level_end = next_level_end
        
        return jumps


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: nums = [2,3,1,1,4] -> Output: 2
    # Jump from index 0 to 1, then to 4
    print(sol.jump([2, 3, 1, 1, 4]))  # 2
    
    # Example 2: nums = [2,3,0,1,4] -> Output: 2
    print(sol.jump([2, 3, 0, 1, 4]))  # 2
    
    # Edge cases
    print(sol.jump([0]))  # 0
    print(sol.jump([1, 2, 3]))  # 2
