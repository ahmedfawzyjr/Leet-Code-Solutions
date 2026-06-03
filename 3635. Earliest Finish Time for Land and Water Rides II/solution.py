from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # To minimize finish time for a pair (i, j):
        # Case 1 (Land then Water): finish = max(landStartTime[i] + landDuration[i], waterStartTime[j]) + waterDuration[j]
        # Case 2 (Water then Land): finish = max(waterStartTime[j] + waterDuration[j], landStartTime[i]) + landDuration[i]
        
        # In Case 1, for any fixed j, we should pick i that minimizes (landStartTime[i] + landDuration[i]).
        # In Case 2, for any fixed i, we should pick j that minimizes (waterStartTime[j] + waterDuration[j]).
        
        min_land_finish = float('inf')
        for start, duration in zip(landStartTime, landDuration):
            min_land_finish = min(min_land_finish, start + duration)
            
        min_water_finish = float('inf')
        for start, duration in zip(waterStartTime, waterDuration):
            min_water_finish = min(min_water_finish, start + duration)
            
        ans = float('inf')
        
        # Optimized Case 1: Land then Water
        for j in range(len(waterStartTime)):
            finish1 = max(min_land_finish, waterStartTime[j]) + waterDuration[j]
            ans = min(ans, finish1)
            
        # Optimized Case 2: Water then Land
        for i in range(len(landStartTime)):
            finish2 = max(min_water_finish, landStartTime[i]) + landDuration[i]
            ans = min(ans, finish2)
            
        return int(ans)
