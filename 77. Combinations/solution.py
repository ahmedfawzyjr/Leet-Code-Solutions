class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        """
        Backtracking approach to generate all combinations of k numbers from 1 to n.
        
        Time: O(k * C(n,k)) - C(n,k) combinations, each of size k
        Space: O(k) for recursion stack (not counting output)
        """
        result = []
        
        def backtrack(start: int, current: list[int]):
            # Base case: if current combination has k elements
            if len(current) == k:
                result.append(current[:])  # Make a copy
                return
            
            # Optimization: we need (k - len(current)) more elements
            # So we can only start from positions where enough elements remain
            # Maximum start position: n - (k - len(current)) + 1
            remaining_needed = k - len(current)
            
            for i in range(start, n - remaining_needed + 2):
                current.append(i)
                backtrack(i + 1, current)
                current.pop()  # Backtrack
        
        backtrack(1, [])
        return result


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    print(f"Test 1: {sol.combine(4, 2)}")
    # Expected: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    
    # Test case 2
    print(f"Test 2: {sol.combine(1, 1)}")
    # Expected: [[1]]
