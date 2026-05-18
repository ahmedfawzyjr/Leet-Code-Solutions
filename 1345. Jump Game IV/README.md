# 1345. Jump Game IV

**Difficulty:** Hard

**Link:** [LeetCode](https://leetcode.com/problems/jump-game-iv/)

## Problem Description

Given an array of integers `arr`, you are initially positioned at the first index of the array.

In one step you can jump from index `i` to index:

- `i + 1` where: `i + 1 < arr.length`.
- `i - 1` where: `i - 1 >= 0`.
- `j` where: `arr[i] == arr[j]` and `i != j`.

Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

### Example 1:
**Input:** `arr = [100,-23,-23,404,100,23,23,3,404]`  
**Output:** `3`  
**Explanation:** You need three jumps from index 0 --> 4 --> 3 --> 8. Note that index 8 is the last index of the array.

### Example 2:
**Input:** `arr = [7]`  
**Output:** `0`  
**Explanation:** Start index is the last index. You do not need to jump.

### Example 3:
**Input:** `arr = [7,6,9,6,9,6,9,7]`  
**Output:** `1`  
**Explanation:** You can jump directly from index 0 to index 7 which is last index of the array.

### Constraints:
- `1 <= arr.length <= 5 * 10^4`
- `-10^8 <= arr[i] <= 10^8`

---

## Solution Analysis

This problem can be modeled as finding the shortest path in an unweighted graph, where each index in the array is a node and each valid jump is an unweighted edge. Because we want the minimum number of steps to reach the destination, **Breadth-First Search (BFS)** is the ideal algorithm.

### Approach: Breadth-First Search (BFS) with Group-Clearing Optimization

Starting from index `0`:
1. **Adjacency Mapping:** Precompute a hash map (`val_to_indices`) grouping indices by their values. This allows $O(1)$ access to all potential teleportation neighbors.
2. **BFS Traversal:** Use a queue to store `(index, steps)` pairs. Keep a `visited` set to prevent cycles and redundant work.
3. **Neighbor Transitions:**
   - Move to `curr - 1` (if in bounds and not visited).
   - Move to `curr + 1` (if in bounds and not visited).
   - Move to any index `j` where `arr[curr] == arr[j]` (if not visited).
4. **Adjacency Clearing (Critical Optimization):** After traversing all indices with the same value as `arr[curr]`, delete `arr[curr]` from the `val_to_indices` map. If we don't do this, a worst-case input with many identical values (e.g., `[7, 7, 7, ..., 7]`) will cause the algorithm to repeatedly iterate over all matching indices, degrading performance to $O(N^2)$. Clearing the mapping guarantees each node and each edge is processed at most once, maintaining a linear runtime.

### Complexity:
- **Time Complexity:** $O(N)$ where $N$ is the number of elements in the array, as every index and every edge is visited at most once.
- **Space Complexity:** $O(N)$ to store the `val_to_indices` map, the queue, and the `visited` set.

---

## Code

Refer to [solution.py](./solution.py) for the complete implementation.
