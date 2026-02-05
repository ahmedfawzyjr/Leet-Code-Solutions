import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        """
        Calculates the minimum number of pigs needed to find the poisonous bucket.
        Formula: (states)^pigs >= buckets
        where states = floor(minutesToTest / minutesToDie) + 1
        
        Time complexity: O(1)
        Space complexity: O(1)
        """
        # states represents how many "rounds" of info one pig can carry
        # e.g., if 4 rounds, a pig can die in round 1, 2, 3, 4, or not at all (5 states)
        states = (minutesToTest // minutesToDie) + 1
        
        # We need to find 'p' such that states^p >= buckets
        # p * log(states) >= log(buckets)
        # p >= log(buckets) / log(states)
        if buckets == 1:
            return 0
            
        return math.ceil(math.log(buckets) / math.log(states))
