from typing import List

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # Sort seeds by growTime in descending order
        # If growTimes are equal, sorting by plantTime doesn't affect the correctness,
        # but sorting by growTime descending is the key.
        seeds = sorted(zip(growTime, plantTime), reverse=True)
        
        max_bloom_day = 0
        current_plant_time = 0
        
        for g, p in seeds:
            current_plant_time += p
            max_bloom_day = max(max_bloom_day, current_plant_time + g)
            
        return max_bloom_day
