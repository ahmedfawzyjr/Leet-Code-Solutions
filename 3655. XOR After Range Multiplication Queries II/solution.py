from typing import List
import collections

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        # Square Root Decomposition on jump size k.
        # Queries with large k are simulated directly.
        # Queries with small k are processed using difference array logic for each k.
        B = 150 
        
        small_k: collections.defaultdict[int, List] = collections.defaultdict(list)
        
        # Separate queries based on k
        for l, r, k, v in queries:
            v %= MOD
            if v == 1:
                continue
            if k > B:
                # Direct simulation for large jump sizes
                if v == 0:
                    for i in range(l, r + 1, k):
                        nums[i] = 0
                else:
                    for i in range(l, r + 1, k):
                        nums[i] = (nums[i] * v) % MOD
            else:
                small_k[int(k)].append((l, r, v))
        
        # Process small jump size queries offline for each distinct k
        for k, qs in small_k.items():
            # nz_diff handles multipliers (non-zero products)
            # z_diff handles the count of zeros introduced at each index
            nz_diff = [1] * (n + k + 1)
            z_diff = [0] * (n + k + 1)
            
            for l, r, v in qs:
                # The query affects indices l, l+k, l+2k, ... such that index <= r.
                # Find the first index after the range that would be hit by l + m*k.
                r_next = l + ((r - l) // k + 1) * k
                
                if v == 0:
                    z_diff[l] += 1
                    if r_next < n + k:
                        z_diff[r_next] -= 1
                else:
                    nz_diff[l] = (nz_diff[l] * v) % MOD
                    v_inv = pow(v, MOD - 2, MOD)
                    if r_next < n + k:
                        nz_diff[r_next] = (nz_diff[r_next] * v_inv) % MOD
            
            # Sweep through the array for the current k. 
            # We jump by k to maintain the modular congruency.
            for offset in range(k):
                curr_multiplier = 1
                curr_zeros = 0
                for i in range(offset, n, k):
                    curr_zeros += z_diff[i]
                    curr_multiplier = (curr_multiplier * nz_diff[i]) % MOD
                    if curr_zeros > 0:
                        nums[i] = 0
                    elif curr_multiplier != 1:
                        nums[i] = (nums[i] * curr_multiplier) % MOD
        
        # The answer is the bitwise XOR of all elements in the final nums array.
        res = 0
        for x in nums:
            res ^= x
        return res
