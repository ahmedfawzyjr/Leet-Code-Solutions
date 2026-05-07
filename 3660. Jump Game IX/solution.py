from typing import List


class Solution:
    def jumpGameIX(self, nums: List[int]) -> List[int]:
        """
        Find the maximum value reachable from each index i.
        
        Rules:
        - Jump Forward (j > i): Allowed if nums[j] < nums[i].
        - Jump Backward (j < i): Allowed if nums[j] > nums[i].
        
        Strategy: Undirected Graph Connectivity
        Two indices i and j (i < j) are connected if nums[i] > nums[j].
        The problem reduces to finding the maximum value in each connected component.
        A boundary at index i exists if max(nums[0...i]) <= min(nums[i+1...n-1]).
        
        Time Complexity: O(n)
        Space Complexity: O(n) for prefix/suffix arrays
        """
        n = len(nums)
        if n == 0:
            return []
            
        # pref_max[i] stores max(nums[0...i])
        pref_max = [0] * n
        pref_max[0] = nums[0]
        for i in range(1, n):
            pref_max[i] = max(pref_max[i-1], nums[i])
            
        # suff_min[i] stores min(nums[i...n-1])
        suff_min = [0] * n
        suff_min[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suff_min[i] = min(suff_min[i+1], nums[i])
            
        ans = [0] * n
        start = 0
        for i in range(n):
            # A block boundary exists at i if max(left) <= min(right)
            if i == n - 1 or pref_max[i] <= suff_min[i+1]:
                # The maximum of this component is pref_max[i]
                current_max = pref_max[i]
                for j in range(start, i + 1):
                    ans[j] = current_max
                start = i + 1
        return ans


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [2, 1, 3]
    print(sol.jumpGameIX(nums1))  # Output: [2, 2, 3]
    
    # Example 2
    nums2 = [2, 3, 1]
    print(sol.jumpGameIX(nums2))  # Output: [3, 3, 3]
    
    # Custom Example
    nums3 = [2, 3, 3, 1]
    print(sol.jumpGameIX(nums3))  # Output: [3, 3, 3, 3]
