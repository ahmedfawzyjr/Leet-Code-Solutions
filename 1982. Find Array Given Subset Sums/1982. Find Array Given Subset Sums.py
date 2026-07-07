from typing import List
from collections import Counter

class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        # Sort the subset sums.
        sums.sort()
        
        # We will reconstruct the array recursively.
        # At each step, sums is of length 2^k.
        # d = sums[1] - sums[0] is the absolute value of one element in the array.
        # We partition sums into A and B of size 2^(k-1) such that B[i] = A[i] + d.
        # One of A or B is the set of subset sums of the remaining elements,
        # which must contain 0.
        # If 0 is in A, then the chosen element is +d, and A is the remaining subset sums.
        # Else, 0 is in B, the chosen element is -d, and B is the remaining subset sums.
        res = []
        
        def solve(curr_sums):
            if len(curr_sums) == 1:
                return
            
            d = curr_sums[1] - curr_sums[0]
            
            # Partition curr_sums into A and B.
            count = Counter(curr_sums)
            A = []
            B = []
            
            for x in curr_sums:
                if count[x] > 0:
                    count[x] -= 1
                    count[x + d] -= 1
                    A.append(x)
                    B.append(x + d)
            
            # Check which partition contains 0
            has_zero_in_A = False
            for val in A:
                if val == 0:
                    has_zero_in_A = True
                    break
            
            if has_zero_in_A:
                res.append(d)
                solve(A)
            else:
                res.append(-d)
                solve(B)
                
        solve(sums)
        return res
