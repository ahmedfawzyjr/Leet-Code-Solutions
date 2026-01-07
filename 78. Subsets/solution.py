class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        Backtracking approach to generate all subsets (power set).
        
        Time: O(n * 2^n) - 2^n subsets, each takes O(n) to copy
        Space: O(n) for recursion stack (not counting output)
        """
        result = []
        
        def backtrack(start: int, current: list[int]):
            # Add the current subset to result (including empty set)
            result.append(current[:])  # Make a copy
            
            # Generate all subsets that include elements from index 'start' onwards
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()  # Backtrack
        
        backtrack(0, [])
        return result
    
    def subsets_iterative(self, nums: list[int]) -> list[list[int]]:
        """
        Iterative approach using cascading.
        For each number, add it to all existing subsets to create new subsets.
        
        Time: O(n * 2^n)
        Space: O(1) (not counting output)
        """
        result = [[]]  # Start with empty set
        
        for num in nums:
            # Add current number to all existing subsets
            result += [subset + [num] for subset in result]
        
        return result


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    print(f"Test 1 (Backtracking): {sol.subsets([1, 2, 3])}")
    # Expected: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    
    print(f"Test 1 (Iterative): {sol.subsets_iterative([1, 2, 3])}")
    
    # Test case 2
    print(f"Test 2: {sol.subsets([0])}")
    # Expected: [[],[0]]
