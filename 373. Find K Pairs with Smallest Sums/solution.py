from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        heap = []
        # Push the first element of nums1 paired with each element of nums2 (up to k)
        # Actually, it's better to push (nums1[i] + nums2[0], i, 0) for i in range(min(k, len(nums1)))
        # This way we explore the matrix of sums row by row or intelligently.
        
        # Min-heap stores tuples: (sum, index_in_nums1, index_in_nums2)
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
            
        result = []
        while heap and len(result) < k:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
                
        return result
