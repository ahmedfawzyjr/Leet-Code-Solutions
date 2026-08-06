from typing import List

class Solution:
    def countRatioSubarrays(self, nums: List[int], a: int, b: int) -> int:
        """
        Calculates the number of valid subarrays where the ratio of even elements (x) 
        to odd elements (y) satisfies x / y <= a / b, with y > 0.
        
        Using prefix counts of even elements E[i] and odd elements O[i]:
        x = E[r+1] - E[l]
        y = O[r+1] - O[l]
        
        The ratio condition x/y <= a/b is equivalent to:
        b * (E[r+1] - E[l]) <= a * (O[r+1] - O[l])
        => b * E[r+1] - a * O[r+1] <= b * E[l] - a * O[l]
        
        Let P[i] = b * E[i] - a * O[i].
        The condition becomes P[r+1] <= P[l] for 0 <= l < r+1 <= n.
        Note that if O[r+1] == O[l] (i.e. y = 0), P[r+1] - P[l] = b * (r+1-l) > 0, 
        so P[r+1] <= P[l] automatically guarantees y > 0.
        
        We can count valid pairs (l, r+1) using coordinate compression and a Binary Indexed Tree (Fenwick Tree).
        """
        n = len(nums)
        P = [0] * (n + 1)
        e_count = 0
        o_count = 0
        
        for i in range(n):
            if nums[i] % 2 == 0:
                e_count += 1
            else:
                o_count += 1
            P[i + 1] = b * e_count - a * o_count
            
        # Coordinate compression
        sorted_vals = sorted(list(set(P)))
        val_to_rank = {val: rank + 1 for rank, val in enumerate(sorted_vals)}
        
        m = len(sorted_vals)
        tree = [0] * (m + 1)
        
        def update(idx: int, val: int):
            while idx <= m:
                tree[idx] += val
                idx += idx & (-idx)
                
        def query(idx: int) -> int:
            s = 0
            while idx > 0:
                s += tree[idx]
                idx -= idx & (-idx)
            return s
            
        ans = 0
        total_inserted = 0
        
        for j in range(n + 1):
            rank = val_to_rank[P[j]]
            # We need the count of previously inserted elements with rank >= current rank
            count_ge = total_inserted - query(rank - 1)
            ans += count_ge
            update(rank, 1)
            total_inserted += 1
            
        return ans
