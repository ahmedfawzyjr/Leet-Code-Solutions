# 3300. Minimum Element After Replacement With Digit Sum

**Difficulty:** Easy

## Problem Description

You are given an integer array `nums`.

You replace each element in `nums` with the **sum of its digits**.

Return the **minimum** element in `nums` after all replacements.

### Example 1:
**Input:** `nums = [10,12,13,14]`  
**Output:** `1`  
**Explanation:** `nums` becomes `[1, 3, 4, 5]` after all replacements, with minimum element 1.

### Example 2:
**Input:** `nums = [1,2,3,4]`  
**Output:** `1`  
**Explanation:** `nums` becomes `[1, 2, 3, 4]` after all replacements, with minimum element 1.

### Example 3:
**Input:** `nums = [999,19,199]`  
**Output:** `10`  
**Explanation:** `nums` becomes `[27, 10, 19]` after all replacements, with minimum element 10.

### Constraints:
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 10^4`

## Solution Approach

The problem asks for the minimum digit sum among all elements in the given array.

1.  **Digit Sum Function:** Create a helper function to calculate the sum of digits of a positive integer. This can be done by repeatedly taking the modulo 10 and dividing by 10.
2.  **Iteration:** Iterate through each number in the input array `nums`.
3.  **Find Minimum:** Calculate the digit sum for each number and keep track of the minimum value found so far.
4.  **Result:** Return the minimum digit sum.

### Complexity Analysis
- **Time Complexity:** $O(N \cdot \log_{10} M)$, where $N$ is the length of the array and $M$ is the maximum value in the array. The number of digits in $M$ is $\lfloor \log_{10} M \rfloor + 1$.
- **Space Complexity:** $O(1)$ as we only store a few variables for the minimum value and the current digit sum.
