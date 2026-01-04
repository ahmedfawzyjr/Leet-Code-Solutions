from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Return all unique permutations of a collection that might contain duplicates.
        
        Sort the array first, then use backtracking with a used[] array.
        Skip duplicates by checking if the previous identical element was used.
        
        Time Complexity: O(n * n!)
        Space Complexity: O(n) for recursion depth
        """
        result = []
        nums.sort()  # Sort to handle duplicates
        used = [False] * len(nums)
        
        def backtrack(current: List[int]):
            if len(current) == len(nums):
                result.append(current[:])
                return
            
            for i in range(len(nums)):
                # Skip if already used
                if used[i]:
                    continue
                
                # Skip duplicates: if current element equals previous AND
                # previous was not used (meaning we're at the same tree level)
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                used[i] = True
                current.append(nums[i])
                backtrack(current)
                current.pop()
                used[i] = False
        
        backtrack([])
        return result


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: nums = [1,1,2] -> [[1,1,2],[1,2,1],[2,1,1]]
    print(sol.permuteUnique([1, 1, 2]))
    
    # Example 2: nums = [1,2,3] -> All 6 permutations
    print(sol.permuteUnique([1, 2, 3]))
