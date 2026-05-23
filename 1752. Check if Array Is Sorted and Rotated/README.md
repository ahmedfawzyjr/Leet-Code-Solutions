# 1752. Check if Array Is Sorted and Rotated

**Difficulty:** Easy

## Problem Description

Given an array `nums`, return `true` if the array was originally sorted in non-decreasing order, then rotated **some** number of positions (including zero). Otherwise, return `false`.

There may be duplicates in the original array.

**Note:** An array `A` rotated by `x` positions results in an array `B` of the same length such that `B[i] == A[(i+x) % A.length]` for every valid index `i`.

### Example 1:
**Input:** `nums = [3,4,5,1,2]`  
**Output:** `true`  
**Explanation:** `[1,2,3,4,5]` is the original sorted array. You can rotate the array by `x = 3` positions to begin on the element of value 3: `[3,4,5,1,2]`.

### Example 2:
**Input:** `nums = [2,1,3,4]`  
**Output:** `false`  
**Explanation:** There is no sorted array once rotated that can make `nums`.

### Example 3:
**Input:** `nums = [1,2,3]`  
**Output:** `true`  
**Explanation:** `[1,2,3]` is the original sorted array. You can rotate the array by `x = 0` positions (i.e. no rotation) to make `nums`.

### Constraints:
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Solution Approach

A sorted array that has been rotated at most once will have at most one point where the current element is greater than the next element (considering the array as circular).

1.  **Count Decreases:** Iterate through the array and count how many times `nums[i] > nums[(i + 1) % n]`.
2.  **Circular Check:** The modulo operator `% n` allows us to check the transition from the last element back to the first element.
3.  **Result:** If the count of such transitions is 0 or 1, then the array is a rotated version of a sorted array.

### Complexity Analysis
- **Time Complexity:** $O(N)$ where $N$ is the length of the array.
- **Space Complexity:** $O(1)$.
