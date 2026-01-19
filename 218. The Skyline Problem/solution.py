from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        A city's skyline is the outer contour of the silhouette formed by all the buildings
        in that city when viewed from a distance.
        Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.
        
        The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:
        
        We can use a sweep-line algorithm.
        We collect all critical points: for each building [L, R, H], we have two events:
        (L, -H, R) -> entering a building of height H
        (R, H, 0) -> leaving a building of height H
        
        We sort these events by x-coordinate. If x-coordinates are the same, we process entering events first
        (smaller height due to negation) to handle edge cases where buildings touch.
        
        We use a max-heap to keep track of the current active buildings' heights.
        """
        # (x, height, right_edge)
        # height is negative for entering event to ensure max-heap behavior with min-heap implementation
        # and also for sorting order (process higher building first at same start point)
        events = []
        for L, R, H in buildings:
            events.append((L, -H, R))
            events.append((R, 0, 0)) # Height 0 is dummy, we only care about removing H
            
        events.sort()
        
        # Max-heap containing (height, right_edge). Initial ground height 0, infinite right edge
        live_buildings = [(0, float('inf'))]
        res = []
        
        for x, h, r in events:
            # If it's an entering event
            if h < 0:
                heapq.heappush(live_buildings, (h, r))
            
            # Remove buildings that have ended before or at current x
            # Since we can't easily remove from heap, we just pop from top if they are invalid
            while live_buildings[0][1] <= x:
                heapq.heappop(live_buildings)
                
            curr_max_height = -live_buildings[0][0]
            
            if not res or res[-1][1] != curr_max_height:
                res.append([x, curr_max_height])
                
        return res
