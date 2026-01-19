from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Given an integer array nums and an integer k, return the kth largest element in the array.
        Note that it is the kth largest element in the sorted order, not the kth distinct element.
        
        We can use a Min-Heap of size k to store the k largest elements seen so far.
        The root of the min-heap will be the smallest among the k largest, which is the kth largest element.
        
        Time Complexity: O(N log k)
        Space Complexity: O(k)
        """
        return heapq.nlargest(k, nums)[-1]
