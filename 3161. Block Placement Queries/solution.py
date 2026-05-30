from typing import List
import bisect

class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (2 * n)
        
    def update(self, i: int, val: int):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])
            
    def query(self, l: int, r: int) -> int:
        l += self.n
        r += self.n
        res = 0
        while l < r:
            if l % 2 == 1:
                res = max(res, self.tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res = max(res, self.tree[r])
            l //= 2
            r //= 2
        return res

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        """
        Solves block placement queries using a Segment Tree for range maximum 
        gap tracking and a sorted list for obstacle management.
        
        Complexity:
        - Time: O(Q * log(M)), where Q is the number of queries and M is the max x.
        - Space: O(M) for the segment tree.
        """
        max_x = 0
        for q in queries:
            max_x = max(max_x, q[1])
        
        M = max_x + 1
        st = SegmentTree(M + 1)
        obstacles = [0, M + 1]
        
        # Initial gap between 0 and a virtual obstacle at M+1
        st.update(M + 1, M + 1)
        
        results = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = bisect.bisect_left(obstacles, x)
                L, R = obstacles[idx - 1], obstacles[idx]
                
                bisect.insort(obstacles, x)
                st.update(x, x - L)
                st.update(R, R - x)
                
            else:
                x, sz = q[1], q[2]
                idx = bisect.bisect_left(obstacles, x)
                L = obstacles[idx - 1]
                
                # Max gap is the max of:
                # 1. Gaps strictly before x
                # 2. The space between the obstacle immediately left of x and x itself
                max_gap = max(st.query(0, L + 1), x - L)
                results.append(max_gap >= sz)
                
        return results
