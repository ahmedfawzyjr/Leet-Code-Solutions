from typing import List, Dict, Tuple
import bisect

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        if n == 0: return 0
        
        # Sort robots and distances together
        combined = sorted(zip(robots, distance))
        r, d = zip(*combined)
        
        # Sort walls for binary search
        walls.sort()
        
        def count_range(L, R):
            # Includes L and R
            if L > R: return 0
            return bisect.bisect_right(walls, R) - bisect.bisect_left(walls, L)
        
        def get_interval_hit(idx_low, idx_high, choice_low, choice_high):
            # choice: 0=L, 1=R, 2=N
            # interval: (r[idx_low], r[idx_high])
            res_set = [] # intervals
            L_bound = r[idx_low] + 1
            R_bound = r[idx_high] - 1
            
            if choice_low == 1: # R
                reach = r[idx_low] + d[idx_low]
                if reach >= L_bound:
                    res_set.append((L_bound, min(R_bound, reach)))
            
            if choice_high == 0: # L
                reach = r[idx_high] - d[idx_high]
                if reach <= R_bound:
                    res_set.append((max(L_bound, reach), R_bound))
            
            if not res_set: return 0
            if len(res_set) == 1:
                return count_range(res_set[0][0], res_set[0][1])
            
            # Union of two intervals: [a, b] and [c, d_] where a <= c
            a, b = res_set[0]
            c, d_ = res_set[1]
            if b >= c: # overlap or adjacent
                return count_range(a, max(b, d_))
            else:
                return count_range(a, b) + count_range(c, d_)

        if n == 1:
            resL = count_range(r[0] - d[0], r[0])
            resR = count_range(r[0], r[0] + d[0])
            return max(resL, resR, 0)
        
        # Choice: 0=L, 1=R, 2=N
        # dp[(c_prev, c_curr)] = max walls hit up to point r[i-1] inclusive
        dp: Dict[Tuple[int, int], int] = {}
        
        # Initial step: i=1. choices for robot 0 and 1.
        for c0 in range(3):
            for c1 in range(3):
                score = 0
                # Walls < r0
                if c0 == 0: # L
                    score += count_range(r[0] - d[0], r[0] - 1)
                # Point r0
                # Hit if c0 != N or (c1=L and d1 >= r1-r0)
                if c0 != 2 or (c1 == 0 and r[1] - d[1] <= r[0]):
                    score += count_range(r[0], r[0])
                # Interval (r0, r1)
                score += get_interval_hit(0, 1, c0, c1)
                
                if (c0, c1) not in dp or score > dp[(c0, c1)]:
                    dp[(c0, c1)] = score
        
        for i in range(2, n):
            new_dp: Dict[Tuple[int, int], int] = {}
            for (c_prev, c_curr), val in dp.items():
                for c_next in range(3):
                    score = val
                    # Point r[i-1]
                    # Hit if c_prev=R and distance covers, or c_curr!=N, or c_next=L and distance covers
                    if c_curr != 2 or (c_prev == 1 and r[i-2] + d[i-2] >= r[i-1]) or (c_next == 0 and r[i] - d[i] <= r[i-1]):
                        score += count_range(r[i-1], r[i-1])
                    # Interval (r[i-1], r[i])
                    score += get_interval_hit(i-1, i, c_curr, c_next)
                    
                    if (c_curr, c_next) not in new_dp or score > new_dp[(c_curr, c_next)]:
                        new_dp[(c_curr, c_next)] = score
            dp = new_dp
            
        # Final step: Point r[n-1] and Interval > r[n-1]
        ans = 0
        for (c_penult, c_last), val in dp.items():
            score = val
            # Point r[n-1]
            if c_last != 2 or (c_penult == 1 and r[n-2] + d[n-2] >= r[n-1]):
                score += count_range(r[n-1], r[n-1])
            # Interval > r[n-1]
            if c_last == 1: # R
                score += count_range(r[n-1] + 1, r[n-1] + d[n-1])
            ans = max(ans, score)
            
        return ans
