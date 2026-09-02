# 3875. Construct Uniform Parity Array I

**Difficulty:** Easy  
**Topics:** Array, Math

## Problem Description

You are given an array `nums1` of `n` distinct integers.

You want to construct another array `nums2` of length `n` such that the elements in `nums2` are either all odd or all even.

For each index `i`, you must choose exactly one of the following (in any order):
- `nums2[i] = nums1[i]`
- `nums2[i] = nums1[i] - nums1[j]`, for an index `j != i`

Return `true` if it is possible to construct such an array, otherwise, return `false`.

---

### Example 1:

**Input:** `nums1 = [2, 3]`  
**Output:** `true`  
**Explanation:**  
- Choose `nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1`
- Choose `nums2[1] = nums1[1] = 3`
- `nums2 = [-1, 3]`, and both elements are odd. Thus, the answer is `true`.

### Example 2:

**Input:** `nums1 = [4, 6]`  
**Output:** `true`  
**Explanation:**  
- Choose `nums2[0] = nums1[0] = 4`
- Choose `nums2[1] = nums1[1] = 6`
- `nums2 = [4, 6]`, and all elements are even. Thus, the answer is `true`.

---

### Constraints:

- $1 \le n == \text{nums1.length} \le 100$
- $1 \le \text{nums1}[i] \le 100$
- `nums1` consists of distinct integers.

---

## Solution Approach

### Mathematical Parity Analysis

We need to decide if we can make all elements in `nums2` have the same parity (either all **even** or all **odd**).

For any index $i$, we have two choices:
1. $nums2[i] = nums1[i]$ (preserves the parity of $nums1[i]$)
2. $nums2[i] = nums1[i] - nums1[j]$ where $j \neq i$

Recall the parity rules for subtraction:
- $\text{even} - \text{even} = \text{even}$
- $\text{odd} - \text{odd} = \text{even}$
- $\text{even} - \text{odd} = \text{odd}$
- $\text{odd} - \text{even} = \text{odd}$

Let's evaluate the feasibility of achieving each target parity:

#### 1. Target: All EVEN
- For any even element $nums1[i]$, we can keep it as is: $nums2[i] = nums1[i]$ ($\text{even}$).
- For any odd element $nums1[i]$, we can subtract another odd element $nums1[j]$ ($j \neq i$): $\text{odd} - \text{odd} = \text{even}$.
- This requires at least one *other* odd number in $nums1$, which is possible if and only if $\text{count(odd)} \neq 1$ (i.e. $\text{count(odd)} = 0$ or $\text{count(odd)} \ge 2$).

#### 2. Target: All ODD
- For any odd element $nums1[i]$, we can keep it as is: $nums2[i] = nums1[i]$ ($\text{odd}$).
- For any even element $nums1[i]$, we can subtract an odd element $nums1[j]$ ($j \neq i$): $\text{even} - \text{odd} = \text{odd}$.
- Since $nums1[i]$ is even, any odd element in $nums1$ is guaranteed to have index $j \neq i$.
- This requires at least one odd number in $nums1$, which is possible if and only if $\text{count(odd)} \ge 1$.

#### 3. Combined Feasibility
- If $\text{count(odd)} = 0$: All elements are already even $\implies$ All-even configuration is possible ($\text{true}$).
- If $\text{count(odd)} = 1$: There is $\ge 1$ odd element $\implies$ All-odd configuration is possible ($\text{true}$).
- If $\text{count(odd)} \ge 2$: Both all-even and all-odd configurations are possible ($\text{true}$).
- For $n = 1$: The single element $nums2[0] = nums1[0]$ is trivially of uniform parity ($\text{true}$).

Therefore, regardless of the input array `nums1`, it is **always possible** to construct a uniform parity array, so we can simply return `true`.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(1)$ - The answer is mathematically always `true`.
- **Space Complexity:** $\mathcal{O}(1)$ - No additional memory required.
