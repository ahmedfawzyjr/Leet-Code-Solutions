from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        # Segment Tree size
        # We need a tree that can cover indices 0 to n-1
        tree_size = 4 * n
        
        # Using lists for the tree nodes: min_val, max_val, lazy_val
        tree_min = [0] * tree_size
        tree_max = [0] * tree_size
        tree_lazy = [0] * tree_size
        
        # Helper check to avoid deeply nested functions
        # This implementation uses recursion. Depth is log(N), so stack overflow is unlikely for N=10^5.
        
        def push(node):
            if tree_lazy[node] != 0:
                lazy_curr = tree_lazy[node]
                
                # Left child
                left = 2 * node
                tree_lazy[left] += lazy_curr
                tree_min[left] += lazy_curr
                tree_max[left] += lazy_curr
                
                # Right child
                right = 2 * node + 1
                tree_lazy[right] += lazy_curr
                tree_min[right] += lazy_curr
                tree_max[right] += lazy_curr
                
                tree_lazy[node] = 0

        def update(node, start, end, l, r, val):
            if l > end or r < start:
                return

            if l <= start and end <= r:
                tree_lazy[node] += val
                tree_min[node] += val
                tree_max[node] += val
                return
            
            push(node)
            mid = (start + end) // 2
            
            update(2 * node, start, mid, l, r, val)
            update(2 * node + 1, mid + 1, end, l, r, val)
            
            tree_min[node] = min(tree_min[2 * node], tree_min[2 * node + 1])
            tree_max[node] = max(tree_max[2 * node], tree_max[2 * node + 1])

        def query_first_zero(node, start, end, limit_r):
            if start > limit_r:
                return -1
            
            # Optimization: If 0 is not in range [min, max], it doesn't exist in this segment
            # Because values change by +1/-1 between adjacent indices, Intermediate Value Theorem applies?
            # Actually, continuity applies to the array indices.
            # So if min > 0 or max < 0, no zero exists.
            if tree_min[node] > 0 or tree_max[node] < 0:
                return -1
            
            if start == end:
                return start if tree_min[node] == 0 else -1
            
            push(node)
            mid = (start + end) // 2
            
            # Try left child first for leftmost
            res = query_first_zero(2 * node, start, mid, limit_r)
            if res != -1:
                return res
            
            # If not in left and within range, try right
            if mid < limit_r:
                return query_first_zero(2 * node + 1, mid + 1, end, limit_r)
            
            return -1

        last_pos = {}
        max_len = 0
        
        for i, num in enumerate(nums):
            val = 1 if num % 2 == 0 else -1
            prev = last_pos.get(num, -1)
            
            # Update range (prev + 1, i) with val
            # This accounts for the new distinct element num in subarrays starting in this range
            update(1, 0, n - 1, prev + 1, i, val)
            
            last_pos[num] = i
            
            # Query the leftmost index L in [0, i] such that value is 0
            # Value 0 means distinct_evens == distinct_odds for subarray nums[L...i]
            left_l = query_first_zero(1, 0, n - 1, i)
            
            if left_l != -1:
                max_len = max(max_len, i - left_l + 1)
                
        return max_len

if __name__ == "__main__":
    sol = Solution()
    print(f"Test Case 1: [2, 5, 4, 3] -> Expected: 4, Got: {sol.longestBalanced([2, 5, 4, 3])}")
    print(f"Test Case 2: [3, 2, 2, 5, 4] -> Expected: 5, Got: {sol.longestBalanced([3, 2, 2, 5, 4])}")
    print(f"Test Case 3: [1, 2, 3, 2] -> Expected: 3, Got: {sol.longestBalanced([1, 2, 3, 2])}")

