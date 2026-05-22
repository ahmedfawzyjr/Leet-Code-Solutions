# 33. Search in Rotated Sorted Array

**Difficulty:** Medium

## Problem Description

There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is **possibly left rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of* `target` *if it is in* `nums`, *or* `-1` *if it is not in* `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

### Example 1:
**Input:** `nums = [4,5,6,7,0,1,2], target = 0`  
**Output:** `4`

### Example 2:
**Input:** `nums = [4,5,6,7,0,1,2], target = 3`  
**Output:** `-1`

### Example 3:
**Input:** `nums = [1], target = 0`  
**Output:** `-1`

### Constraints:
- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are **unique**.
- `nums` is an ascending array that is possibly rotated.
- `-10^4 <= target <= 10^4`

## Solution Approach

To achieve `O(log n)` time complexity, we use a modified **Binary Search**.

1.  **Identify Sorted Half:** In a rotated sorted array, at least one half (left or right) relative to the middle element will always be sorted.
2.  **Range Check:** 
    - If the left half `[left, mid]` is sorted:
        - Check if the target is within `nums[left]` and `nums[mid]`.
        - If yes, search in the left half; otherwise, search in the right half.
    - If the right half `[mid, right]` is sorted:
        - Check if the target is within `nums[mid]` and `nums[right]`.
        - If yes, search in the right half; otherwise, search in the left half.
3.  **Iterate:** Continue until the target is found or the pointers cross.

### Complexity Analysis
- **Time Complexity:** $O(\log N)$ as we halve the search space in each step.
- **Space Complexity:** $O(1)$ as we only use a few pointers.
