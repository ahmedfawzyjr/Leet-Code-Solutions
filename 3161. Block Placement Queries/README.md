# 3161. Block Placement Queries

**Difficulty:** Hard

## Problem Description

There exists an infinite number line, with its origin at 0 and extending towards the **positive** x-axis.

You are given a 2D array `queries`, which contains two types of queries:

1.  For a query of type 1, `queries[i] = [1, x]`. Build an obstacle at distance `x` from the origin. It is guaranteed that there is **no** obstacle at distance `x` when the query is asked.
2.  For a query of type 2, `queries[i] = [2, x, sz]`. Check if it is possible to place a block of size `sz` anywhere in the range `[0, x]` on the line, such that the block **entirely** lies in the range `[0, x]`. A block **cannot** be placed if it intersects with any obstacle, but it may touch it. Note that you do **not** actually place the block. Queries are separate.

Return a boolean array `results`, where `results[i]` is `true` if you can place the block specified in the $i^{th}$ query of type 2, and `false` otherwise.

### Example 1:
**Input:** `queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]`  
**Output:** `[false,true,true]`  
**Explanation:** 
- After `[1, 2]`, there is an obstacle at `x = 2`.
- For `[2, 3, 3]`, we need space of 3 in `[0, 3]`. Only `[0, 2]` and `[2, 3]` are free, max space is 2. So `false`.
- For `[2, 3, 1]`, max space is 2, so `true`.
- For `[2, 2, 2]`, we need space of 2 in `[0, 2]`. `[0, 2]` is free. So `true`.

### Constraints:
- `1 <= queries.length <= 5 * 10^4`
- `queries[i].length <= 3`
- `1 <= x <= min(5 * 10^4, 3 * queries.length)`
- `1 <= sz <= x`
- The input is generated such that there is at least one query of type 2.

## Solution Approach

To find if a block of size `sz` can fit in `[0, x]`, we need the **maximum gap** between consecutive obstacles (including 0) that is within the range `[0, x]`.

1.  **Obstacle Management:** Use a sorted list (with `bisect`) to track the positions of obstacles.
2.  **Max Gap Tracking:** Use a **Segment Tree** to store and query the maximum gap.
    - Each leaf `st[i]` in the segment tree represents the distance between the obstacle at `i` and the one immediately to its left.
    - When an obstacle is added at `x`, find its neighbors `L` and `R`.
    - Update `st[x] = x - L` and `st[R] = R - x`.
3.  **Querying:** For a query `[2, x, sz]`:
    - Find the obstacle `L` immediately to the left of `x`.
    - The maximum gap in `[0, x]` is `max(SegmentTree.query(0, L), x - L)`.
    - Return `true` if this value is $\ge sz$.

### Complexity Analysis
- **Time Complexity:** $O(Q \cdot \log M)$, where $Q$ is the number of queries and $M$ is the maximum coordinate ($5 \cdot 10^4$).
- **Space Complexity:** $O(M)$ for the segment tree.
