# 153. Find Minimum in Rotated Sorted Array

## Problem Description

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
- `[4,5,6,7,0,1,2]` if it was rotated 4 times.
- `[0,1,2,4,5,6,7]` if it was rotated 7 times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.

You must write an algorithm that runs in `O(log n)` time.

### Example 1
**Input:** `nums = [3,4,5,1,2]`  
**Output:** `1`  
**Explanation:** The original array was `[1,2,3,4,5]` rotated 3 times.

### Example 2
**Input:** `nums = [4,5,6,7,0,1,2]`  
**Output:** `0`  
**Explanation:** The original array was `[0,1,2,4,5,6,7]` and it was rotated 4 times.

### Example 3
**Input:** `nums = [11,13,15,17]`  
**Output:** `11`  
**Explanation:** The original array was `[11,13,15,17]` and it was rotated 4 times.

## Constraints
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are **unique**.
- `nums` is sorted and rotated between `1` and `n` times.

## Solution

### Approach: Binary Search
The array is sorted but rotated. We can use binary search to find the point where the rotation happens (the minimum element).

1. Initialize `left = 0` and `right = n - 1`.
2. While `left < right`:
   - Calculate `mid = (left + right) // 2`.
   - If `nums[mid] > nums[right]`, it means the minimum is in the right half (excluding `mid`). So, `left = mid + 1`.
   - Else, the minimum is either at `mid` or in the left half. So, `right = mid`.
3. After the loop, `left` will point to the minimum element.

### Complexity Analysis
- **Time Complexity:** $O(\log n)$ because we are using binary search.
- **Space Complexity:** $O(1)$ as we only use a few pointers.
