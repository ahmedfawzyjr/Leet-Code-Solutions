from typing import List

class BIT:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)
        
    def update(self, idx: int, val: int):
        while idx <= self.n:
            self.tree[idx] += val
            idx += idx & (-idx)
            
    def query(self, idx: int) -> int:
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & (-idx)
        return s

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        # Mapping from value to its index in nums1
        idx_in_nums1 = {val: i for i, val in enumerate(nums1)}
        
        # A[i] is the index of nums2[i] in nums1
        A = [idx_in_nums1[x] for x in nums2]
        
        bit = BIT(n)
        ans = 0
        
        for j in range(n):
            val = A[j]
            # Find elements to the left of j that are smaller than val
            # BIT is 1-indexed, so we query val (which represents count of elements in range [0, val-1] in 0-indexed terms)
            left_smaller = bit.query(val)
            
            # Since A is a permutation of [0, ..., n-1], there are exactly val elements smaller than val in total.
            # Thus, the number of elements to the right of j that are smaller than val is (val - left_smaller).
            # The total elements to the right of j is (n - 1 - j).
            # So elements to the right of j that are larger than val is:
            right_larger = (n - 1 - j) - (val - left_smaller)
            
            ans += left_smaller * right_larger
            
            # Insert the current element into the BIT (1-indexed, so val + 1)
            bit.update(val + 1, 1)
            
        return ans
