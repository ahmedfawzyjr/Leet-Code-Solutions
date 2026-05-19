# 2540. Minimum Common Value

**Difficulty:** Easy

**Link:** [LeetCode](https://leetcode.com/problems/minimum-common-value/)

## Problem Description

Given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, return the **minimum integer common** to both arrays. If there is no common integer amongst `nums1` and `nums2`, return `-1`.

Note that an integer is said to be common to `nums1` and `nums2` if both arrays have **at least one** occurrence of that integer.

### Example 1:
**Input:** `nums1 = [1,2,3], nums2 = [2,4]`  
**Output:** `2`  
**Explanation:** The smallest element common to both arrays is 2, so we return 2.

### Example 2:
**Input:** `nums1 = [1,2,3,6], nums2 = [2,3,4,5]`  
**Output:** `2`  
**Explanation:** There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.

### Constraints:
- `1 <= nums1.length, nums2.length <= 10^5`
- `1 <= nums1[i], nums2[j] <= 10^9`
- Both `nums1` and `nums2` are sorted in **non-decreasing** order.

---

## Solution Analysis

Since both arrays are already sorted in non-decreasing order, we can solve this problem highly efficiently.

### Approach 1: Two Pointers (Optimal)

Using the sorted property, we can place a pointer at the beginning of each array:
1. Initialize two pointers, `i = 0` (for `nums1`) and `j = 0` (for `nums2`).
2. Compare the elements at the current pointers, `nums1[i]` and `nums2[j]`:
   - **If they are equal (`nums1[i] == nums2[j]`):** We found our common element! Since we traverse the arrays from smallest to largest, this first match is guaranteed to be the minimum common value. Return `nums1[i]`.
   - **If `nums1[i] < nums2[j]`:** The element in `nums1` is too small to match the current element in `nums2`. Since the arrays are sorted, increment `i` to look for a larger value.
   - **If `nums1[i] > nums2[j]`:** The element in `nums2` is too small to match the current element in `nums1`. Increment `j` to look for a larger value in `nums2`.
3. If either pointer runs out of bounds without finding a match, return `-1`.

#### Complexity:
- **Time Complexity:** $O(N_1 + N_2)$ where $N_1$ and $N_2$ are the lengths of `nums1` and `nums2` respectively. In the worst case, we traverse each array at most once.
- **Space Complexity:** $O(1)$ auxiliary space, as we only need two pointer variables.

---

### Alternative Approaches

#### 1. Binary Search
For each element in `nums1`, binary search it in `nums2`.
- **Complexity:** $O(N_1 \log N_2)$ time and $O(1)$ space. Useful if one array is extremely small compared to the other (e.g., $N_1 \ll N_2$).

#### 2. Hash Set / Hash Map
Store all elements of one array in a hash set, then iterate through the other array to find the first matching element.
- **Complexity:** $O(N_1 + N_2)$ time and $O(N_1)$ space. Less optimal than the two-pointer approach due to the $O(N_1)$ extra space requirement.

---

## Code

Refer to [solution.py](./solution.py) for the complete implementation.
