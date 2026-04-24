class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # Count L, R and _
        l_count = moves.count('L')
        r_count = moves.count('R')
        underscore_count = moves.count('_')
        
        # To maximize distance, all '_' should go in the direction 
        # that already has more moves (or any direction if they are equal)
        return abs(l_count - r_count) + underscore_count
