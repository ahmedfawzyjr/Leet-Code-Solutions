
import math
import heapq

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        # Build sparse tables for min and max
        log_table = [0] * (n + 1)
        for i in range(2, n + 1):
            log_table[i] = log_table[i // 2] + 1
        
        K = log_table[n] + 1
        st_min = [[0] * n for _ in range(K)]
        st_max = [[0] * n for _ in range(K)]
        
        for i in range(n):
            st_min[0][i] = nums[i]
            st_max[0][i] = nums[i]
        
        for j in range(1, K):
            for i in range(n - (1 << j) + 1):
                st_min[j][i] = min(st_min[j-1][i], st_min[j-1][i + (1 << (j-1))])
                st_max[j][i] = max(st_max[j-1][i], st_max[j-1][i + (1 << (j-1))])
        
        def get_diff(l, r):
            length = r - l + 1
            k_log = log_table[length]
            min_val = min(st_min[k_log][l], st_min[k_log][r - (1 << k_log) + 1])
            max_val = max(st_max[k_log][l], st_max[k_log][r - (1 << k_log) + 1])
            return max_val - min_val
        
        # Max heap: store (-diff, l, r) to simulate max-heap using min-heap
        heap = []
        visited = set()
        
        # Initialize heap with all [i, n-1]
        for i in range(n):
            diff = get_diff(i, n-1)
            heapq.heappush(heap, (-diff, i, n-1))
            visited.add((i, n-1))
        
        result = 0
        
        for _ in range(k):
            neg_diff, l, r = heapq.heappop(heap)
            result += -neg_diff
            
            # Add [l, r-1]
            if l <= r-1 and (l, r-1) not in visited:
                new_diff = get_diff(l, r-1)
                heapq.heappush(heap, (-new_diff, l, r-1))
                visited.add((l, r-1))
            
            # Add [l+1, r]
            if l+1 <= r and (l+1, r) not in visited:
                new_diff = get_diff(l+1, r)
                heapq.heappush(heap, (-new_diff, l+1, r))
                visited.add((l+1, r))
        
        return result
