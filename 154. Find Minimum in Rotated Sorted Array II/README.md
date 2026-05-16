# 154. Find Minimum in Rotated Sorted Array II

**Difficulty:** Hard

**Link:** [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

## Problem Description

Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,4,4,5,6,7]` might become:

- `[4,5,6,7,0,1,4]` if it was rotated `4` times.
- `[0,1,4,4,5,6,7]` if it was rotated `7` times.

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` that may contain **duplicates**, return the *minimum element* of this array.

You must decrease the overall operation steps as much as possible.

### Example 1:
**Input:** `nums = [1,3,5]`
**Output:** `1`

### Example 2:
**Input:** `nums = [2,2,2,0,1]`
**Output:** `0`

### Constraints:
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- `nums` is sorted and rotated between `1` and `n` times.

---

## Solution Analysis

This problem is an extension of [153. Find Minimum in Rotated Sorted Array](./../153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array), with the added complexity of **duplicates**.

### Approach: Binary Search

In a standard rotated sorted array without duplicates, we can always decide which half to search by comparing `nums[mid]` with `nums[right]`. However, with duplicates, if `nums[mid] == nums[right]`, we cannot be certain where the minimum lies. 

For example:
- `[1, 0, 1, 1, 1]` -> `mid` is 1, `right` is 1. Min is in the left.
- `[1, 1, 1, 0, 1]` -> `mid` is 1, `right` is 1. Min is in the right.

In this case, the best we can do is decrement the `right` pointer by 1 (`right -= 1`) and continue the search. This maintains the invariant that the minimum element is still within the range `[left, right]`.

### Complexity:
- **Time Complexity:** $O(\log n)$ on average, but $O(n)$ in the worst case (e.g., all elements are the same except one).
- **Space Complexity:** $O(1)$ as we only use a few pointers.
