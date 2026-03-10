# 3130. Find All Possible Stable Binary Arrays II

**Link**: [https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/](https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/)

## Problem Description

You are given 3 positive integers `zero`, `one`, and `limit`.

A binary array `arr` is called **stable** if:
- The number of occurrences of 0 in `arr` is **exactly** `zero`.
- The number of occurrences of 1 in `arr` is **exactly** `one`.
- Each subarray of `arr` with a size greater than `limit` must contain **both** 0 and 1.

Return the total number of **stable** binary arrays.

Since the answer may be very large, return it **modulo** $10^9 + 7$.

---

## Solution Explanation

### Approach: Dynamic Programming (Optimized)

The problem asks us to count arrangements with constraints on consecutive identical elements. This is a classic DP problem.

#### 1. State Definition
Let:
- `dp0[i][j]` be the number of stable arrays with `i` zeros and `j` ones ending with a `0`.
- `dp1[i][j]` be the number of stable arrays with `i` zeros and `j` ones ending with a `1`.

#### 2. Recurrence Relations
To form a stable array of `(i, j)` ending in `0`, we can append between `1` to `limit` zeros to a stable array of `(i-k, j)` that ends in `1`.
$$dp0[i][j] = \sum_{k=1}^{limit} dp1[i-k][j]$$
Symmetrically:
$$dp1[i][j] = \sum_{k=1}^{limit} dp0[i][j-k]$$

#### 3. Optimization
The naive calculation of these sums would lead to $O(zero \cdot one \cdot limit)$, which is too slow ($1000^3$).
We can optimize the transition to $O(1)$ by using the previous state:
$$dp0[i][j] = dp0[i-1][j] + dp1[i-1][j] - dp1[i-limit-1][j]$$
This identifies that the sum for `i` is the same as the sum for `i-1` plus the new `dp1` term, minus the oldest `dp1` term that now exceeds the `limit`.

### Complexity
- **Time Complexity**: $O(zero \times one)$ - We fill a 2D table of size $zero \times one$ with $O(1)$ transitions.
- **Space Complexity**: $O(zero \times one)$ - To store the DP tables.
