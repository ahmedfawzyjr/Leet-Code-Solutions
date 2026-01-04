from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Return all possible permutations of distinct integers.
        
        Backtracking approach: Build permutations by choosing each unused element.
        
        Time Complexity: O(n * n!)
        Space Complexity: O(n) for recursion depth
        """
        result = []
        
        def backtrack(current: List[int], remaining: List[int]):
            if not remaining:
                result.append(current[:])
                return
            
            for i in range(len(remaining)):
                # Choose the i-th element
                current.append(remaining[i])
                # Recurse with remaining elements (excluding chosen)
                backtrack(current, remaining[:i] + remaining[i + 1:])
                # Backtrack
                current.pop()
        
        backtrack([], nums)
        return result
    
    def permute_swap(self, nums: List[int]) -> List[List[int]]:
        """
        Alternative: In-place swapping approach.
        
        Time Complexity: O(n * n!)
        Space Complexity: O(n) for recursion depth
        """
        result = []
        
        def backtrack(start: int):
            if start == len(nums):
                result.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                # Swap to place nums[i] at position start
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                # Swap back (backtrack)
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return result


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: nums = [1,2,3]
    print(sol.permute([1, 2, 3]))
    # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    
    # Example 2: nums = [0,1]
    print(sol.permute([0, 1]))  # [[0,1],[1,0]]
    
    # Example 3: nums = [1]
    print(sol.permute([1]))  # [[1]]
