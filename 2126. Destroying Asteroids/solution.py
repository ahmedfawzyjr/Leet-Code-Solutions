from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        """
        Determines if all asteroids can be destroyed by a planet with initial mass.
        Optimal strategy: Destroy smaller asteroids first (Greedy).
        
        Complexity:
        - Time: O(N log N) for sorting, where N is the number of asteroids.
        - Space: O(1) or O(N) depending on the sorting algorithm implementation.
        """
        # Sort asteroids in ascending order to destroy smaller ones first
        asteroids.sort()
        
        current_mass = mass
        for a_mass in asteroids:
            if current_mass >= a_mass:
                current_mass += a_mass
            else:
                # Planet is destroyed
                return False
                
        return True
