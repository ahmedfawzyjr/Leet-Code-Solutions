# 1306. Jump Game III

**Difficulty:** Medium

**Link:** [LeetCode](https://leetcode.com/problems/jump-game-iii/)

## Problem Description

Given an array of non-negative integers `arr`, you are initially positioned at `start` index of the array. When you are at index `i`, you can jump to `i + arr[i]` or `i - arr[i]`, check if you can reach **any** index with value 0.

Notice that you can not jump outside of the array at any time.

### Example 1:
**Input:** `arr = [4,2,3,0,3,1,2]`, `start = 5`  
**Output:** `true`  
**Explanation:**  
All possible ways to reach at index 3 with value 0 are:  
- index 5 -> index 4 -> index 1 -> index 3  
- index 5 -> index 6 -> index 4 -> index 1 -> index 3  

### Example 2:
**Input:** `arr = [4,2,3,0,3,1,2]`, `start = 0`  
**Output:** `true`  
**Explanation:**  
One possible way to reach at index 3 with value 0 is:  
- index 0 -> index 4 -> index 1 -> index 3  

### Example 3:
**Input:** `arr = [3,0,2,1,2]`, `start = 2`  
**Output:** `false`  
**Explanation:** There is no way to reach at index 1 with value 0.  

### Constraints:
- `1 <= arr.length <= 5 * 10^4`
- `0 <= arr[i] < arr.length`
- `0 <= start < arr.length`

---

## Solution Analysis

This problem can be modeled as a **Graph Traversal** problem (either BFS or DFS), where each index represents a node, and the valid jumps represent directed edges to other nodes (indices).

### Approach 1: Breadth-First Search (BFS)

We can use a queue to traverse the array iteratively. Starting from the `start` index:
1. Initialize a queue with the `start` index and a `visited` set to avoid infinite loops and redundant exploration.
2. While the queue is not empty, pop the current index.
3. If `arr[curr] == 0`, we have successfully reached a target index, so return `true`.
4. Otherwise, calculate the two possible jump destinations: `curr + arr[curr]` and `curr - arr[curr]`.
5. If they are within the bounds of the array and have not been visited yet, mark them as visited and add them to the queue.
6. If the queue becomes empty and we haven't found any index with value 0, return `false`.

### Complexity:
- **Time Complexity:** $O(N)$ where $N$ is the length of the array, since we visit each index at most once.
- **Space Complexity:** $O(N)$ for the queue and the `visited` set.

---

## Code

Refer to [solution.py](./solution.py) for the complete implementation.
