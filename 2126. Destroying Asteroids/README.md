# 2126. Destroying Asteroids

**Difficulty:** Medium

## Problem Description

You are given an integer `mass`, which represents the original mass of a planet. You are further given an integer array `asteroids`, where `asteroids[i]` is the mass of the $i^{th}$ asteroid.

You can arrange for the planet to collide with the asteroids in **any arbitrary order**. If the mass of the planet is **greater than or equal to** the mass of the asteroid, the asteroid is destroyed and the planet **gains** the mass of the asteroid. Otherwise, the planet is destroyed.

Return `true` *if all asteroids can be destroyed. Otherwise, return* `false`.

### Example 1:
**Input:** `mass = 10, asteroids = [3,9,19,5,21]`  
**Output:** `true`  
**Explanation:** One way to order the asteroids is `[9,19,5,3,21]`:
- The planet collides with the asteroid with a mass of 9. New planet mass: 10 + 9 = 19
- The planet collides with the asteroid with a mass of 19. New planet mass: 19 + 19 = 38
- The planet collides with the asteroid with a mass of 5. New planet mass: 38 + 5 = 43
- The planet collides with the asteroid with a mass of 3. New planet mass: 43 + 3 = 46
- The planet collides with the asteroid with a mass of 21. New planet mass: 46 + 21 = 67
All asteroids are destroyed.

### Example 2:
**Input:** `mass = 5, asteroids = [4,9,23,4]`  
**Output:** `false`  
**Explanation:** 
The planet cannot ever gain enough mass to destroy the asteroid with a mass of 23.
After the planet destroys the other asteroids, it will have a mass of 5 + 4 + 9 + 4 = 22.
This is less than 23, so a collision would not destroy the last asteroid.

### Constraints:
- `1 <= mass <= 10^5`
- `1 <= asteroids.length <= 10^5`
- `1 <= asteroids[i] <= 10^5`

## Solution Approach

This is a classic **Greedy** problem. To maximize the planet's mass at any point, we should always aim to destroy the smallest available asteroid that we can currently handle.

1.  **Sorting:** Sort the `asteroids` array in non-decreasing order.
2.  **Iterative Gain:** Iterate through the sorted asteroids. For each asteroid:
    - If `current_mass >= asteroid_mass`, add the asteroid's mass to `current_mass`.
    - Otherwise, it's impossible to destroy this asteroid (and any larger ones), so return `false`.
3.  **Completion:** If we successfully iterate through all asteroids, return `true`.

### Complexity Analysis
- **Time Complexity:** $O(N \log N)$, where $N$ is the number of asteroids, primarily due to sorting.
- **Space Complexity:** $O(1)$ (ignoring space used by sorting) as we only use a single variable to track current mass.
