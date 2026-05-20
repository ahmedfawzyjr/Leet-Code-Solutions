# 2657. Find the Prefix Common Array of Two Arrays

**Difficulty:** Medium

**Link:** [LeetCode](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/)

## Problem Description

You are given two **0-indexed** integer permutations `A` and `B` of length `n`.

A **prefix common array** of `A` and `B` is an array `C` such that `C[i]` is equal to the count of numbers that are present at or before the index `i` in both `A` and `B`.

Return *the prefix common array of* `A` and `B`.

A sequence of `n` integers is called a **permutation** if it contains all integers from `1` to `n` exactly once.

### Example 1:
**Input:** `A = [1,3,2,4], B = [3,1,2,4]`  
**Output:** `[0,2,3,4]`  
**Explanation:**  
- At `i = 0`: no number is common, so `C[0] = 0`.  
- At `i = 1`: 1 and 3 are common in `A` and `B`, so `C[1] = 2`.  
- At `i = 2`: 1, 2, and 3 are common in `A` and `B`, so `C[2] = 3`.  
- At `i = 3`: 1, 2, 3, and 4 are common in `A` and `B`, so `C[3] = 4`.

### Example 2:
**Input:** `A = [2,3,1], B = [3,1,2]`  
**Output:** `[0,1,3]`  
**Explanation:**  
- At `i = 0`: no number is common, so `C[0] = 0`.  
- At `i = 1`: only 3 is common in `A` and `B`, so `C[1] = 1`.  
- At `i = 2`: 1, 2, and 3 are common in `A` and `B`, so `C[2] = 3`.

### Constraints:
- `1 <= A.length == B.length == n <= 50`
- `1 <= A[i], B[i] <= n`
- It is guaranteed that `A` and `B` are both permutations of `n` integers.

---

## Solution Analysis

Since both `A` and `B` are permutations of `n` integers, we can solve this problem very efficiently using a Hash Set or a frequency array to keep track of the elements we have seen as we iterate.

### Approach: Hash Set (Optimal Tracking)

We can iterate through both arrays simultaneously from index `0` to `n - 1`:
1. Keep a set `seen` of all elements encountered so far from both arrays `A` and `B`.
2. Maintain a running count `common` of elements that have been seen in both arrays.
3. For each index `i`:
   - Check if `A[i]` is already in `seen`. If it is, this means `A[i]` was previously seen in `B` (since elements in `A` are unique). Increment `common`. Otherwise, add `A[i]` to `seen`.
   - Check if `B[i]` is already in `seen`. If it is, this means `B[i]` was previously seen in `A` (since elements in `B` are unique). Increment `common`. Otherwise, add `B[i]` to `seen`.
   - Append the current `common` to our result array `C`.
4. Return `C`.

#### Complexity:
- **Time Complexity:** $O(n)$ where $n$ is the length of arrays `A` and `B`. We perform a single pass over the arrays, and all set operations (lookup and insertion) take $O(1)$ time on average.
- **Space Complexity:** $O(n)$ auxiliary space to store the `seen` hash set, which will contain at most $2n$ elements.

---

## Code

Refer to [solution.py](./solution.py) for the complete implementation.
