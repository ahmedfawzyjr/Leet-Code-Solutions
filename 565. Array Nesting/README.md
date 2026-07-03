# 565. Array Nesting

**Difficulty:** Medium

## Problem Description

You are given an integer array `nums` of length `n` where `nums` is a permutation of the numbers in the range `[0, n - 1]`.

You should build a set `s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... }` subjected to the following rule:
- The first element in `s[k]` starts with the selection of the element `nums[k]` of index `= k`.
- The next element in `s[k]` should be `nums[nums[k]]`, and then `nums[nums[nums[k]]]`, and so on.
- We stop adding right before a duplicate element occurs in `s[k]`.

Return the *longest* length of a set `s[k]`.

### Example 1:
- **Input:** `nums = [5,4,0,3,1,6,2]`
- **Output:** `4`
- **Explanation:** 
  `nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.`
  One of the longest sets `s[k]`:
  `s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}`

### Example 2:
- **Input:** `nums = [0,1,2]`
- **Output:** `1`

### Constraints:
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] < nums.length`
- All the values of `nums` are **unique**.

## Solution Approach

Since the array `nums` is a permutation of numbers in the range `[0, n - 1]`, we can view it as a directed graph where each index `i` has a single outgoing edge to `nums[i]`. Because it's a permutation, every vertex has exactly one incoming edge and one outgoing edge. This means the graph decomposes into a set of disjoint cycles.

To find the longest cycle:
1.  **Traverse** the array from left to right.
2.  For each unvisited index, traverse the cycle starting at that index, keeping track of the count of visited nodes.
3.  **Mark** visited indices in-place by setting `nums[curr] = -1` to avoid traversing any cycle more than once.
4.  Keep track of the maximum cycle length found.

## Complexity Analysis

- **Time Complexity:** $O(N)$, where $N$ is the length of `nums`. Each element is visited at most twice (once in the outer loop, and once during cycle traversal).
- **Space Complexity:** $O(1)$ auxiliary space, since we modify the input array in-place to mark visited nodes.
