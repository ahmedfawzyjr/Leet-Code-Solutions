from typing import List
from collections import Counter

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for p1 in points:
            dists = []
            for p2 in points:
                if p1 == p2:
                    continue
                # Use squared distance to avoid floating point issues
                d = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
                dists.append(d)
            
            counts = Counter(dists)
            for d in counts:
                # For m points at same distance, we can pick any 2 in m*(m-1) ways
                m = counts[d]
                res += m * (m - 1)
        return res
