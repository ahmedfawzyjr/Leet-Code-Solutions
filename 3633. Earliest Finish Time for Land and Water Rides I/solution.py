from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_finish_time = float('inf')
        
        n = len(landStartTime)
        m = len(waterStartTime)
        
        for i in range(n):
            for j in range(m):
                # Case 1: Land ride then Water ride
                # Land finish time
                land_finish = landStartTime[i] + landDuration[i]
                # Water start time is max of land finish and its own opening time
                water_start = max(land_finish, waterStartTime[j])
                # Final finish time
                finish1 = water_start + waterDuration[j]
                
                # Case 2: Water ride then Land ride
                # Water finish time
                water_finish = waterStartTime[j] + waterDuration[j]
                # Land start time is max of water finish and its own opening time
                land_start = max(water_finish, landStartTime[i])
                # Final finish time
                finish2 = land_start + landDuration[i]
                
                min_finish_time = min(min_finish_time, finish1, finish2)
                
        return min_finish_time
