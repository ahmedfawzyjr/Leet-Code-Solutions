from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def get_p(x, y):
            if y == 0: return x
            if x == side: return side + y
            if y == side: return 2 * side + (side - x)
            if x == 0: return 3 * side + (side - y)
            return 0
        
        # Sort points by perimeter position
        p_list = []
        for x, y in points:
            p_list.append((get_p(x, y), x, y))
        p_list.sort()
        
        n = len(p_list)
        # Double the points for circularity
        extended_points = p_list + [(p + 4 * side, x, y) for p, x, y in p_list]
        num_extended = len(extended_points)
        
        def check(d):
            # next_idx[i] is the first j > i such that Manhattan distance(Pi, Pj) >= d
            # Since d <= side (for k >= 4), the Manhattan distance is monotonic
            # in the relevant range (at most halfway around the square).
            next_idx = [0] * num_extended
            r = 0
            for i in range(num_extended):
                if r <= i: r = i + 1
                xi, yi = extended_points[i][1], extended_points[i][2]
                while r < num_extended:
                    xr, yr = extended_points[r][1], extended_points[r][2]
                    if abs(xi - xr) + abs(yi - yr) >= d:
                        break
                    r += 1
                next_idx[i] = r
                
            # Try starting from points within the first gap.
            # Any valid solution must have at least one point in the first 'jump' interval.
            limit = next_idx[0]
            if limit > n: limit = n
            
            for i in range(limit + 1):
                curr = i
                possible = True
                for _ in range(k - 1):
                    curr = next_idx[curr]
                    if curr >= i + n:
                        possible = False
                        break
                
                if possible:
                    # check distance from P_curr back to P_i
                    xi, yi = extended_points[i][1], extended_points[i][2]
                    xk, yk = extended_points[curr][1], extended_points[curr][2]
                    if abs(xi - xk) + abs(yi - yk) >= d:
                        return True
            return False

        low = 1
        high = side
        ans = 0
        while low <= high:
            # For d=0, it's always possible but constraints say d > 0
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
