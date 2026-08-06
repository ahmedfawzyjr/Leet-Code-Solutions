# 4013. Count Subarrays With Even Odd Ratio II

**Difficulty:** Hard

**Link:** [LeetCode](https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/)

## Problem Description

You are given an integer array `nums` and two integers `a` and `b`.

For a subarray, let:
- `x` be the number of even elements.
- `y` be the number of odd elements.

The ratio of even to odd elements in a subarray is defined as `x / y`, where ratios are compared by their exact rational values.

A subarray is considered valid if:
- `y > 0`, and
- `x / y <= a / b`.

Return the number of valid subarrays in `nums`.

### Example 1:
**Input:** `nums = [1, 2, 1, 2]`, `a = 2`, `b = 2`  
**Output:** `7`  
**Explanation:**  
The valid subarrays with ratio $x / y \le 2/2 = 1$ and $y > 0$ are:
- `nums[0..0]` = `[1]` (ratio $0/1 \le 1$)
- `nums[0..1]` = `[1, 2]` (ratio $1/1 \le 1$)
- `nums[0..2]` = `[1, 2, 1]` (ratio $1/2 \le 1$)
- `nums[0..3]` = `[1, 2, 1, 2]` (ratio $2/2 \le 1$)
- `nums[1..2]` = `[2, 1]` (ratio $1/1 \le 1$)
- `nums[2..2]` = `[1]` (ratio $0/1 \le 1$)
- `nums[2..3]` = `[1, 2]` (ratio $1/1 \le 1$)

### Example 2:
**Input:** `nums = [2, 2, 1]`, `a = 2`, `b = 1`  
**Output:** `3`  
**Explanation:**  
The valid subarrays are `nums[0..2] = [2, 2, 1]` (ratio 2/1), `nums[1..2] = [2, 1]` (ratio 1/1), and `nums[2..2] = [1]` (ratio 0/1).

### Example 3:
**Input:** `nums = [2, 2, 2]`, `a = 1`, `b = 1`  
**Output:** `0`  
**Explanation:**  
Every subarray contains 0 odd elements ($y = 0$), so no subarray is valid.

### Constraints:
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= a, b <= 10^9`

---

## Solution Analysis

### Prefix Transformation + Binary Indexed Tree (Fenwick Tree)

#### Mathematical Derivation:
Let $E[i]$ and $O[i]$ be the prefix counts of even and odd numbers in `nums[0..i-1]`.
For a subarray `nums[l..r]` (with $0 \le l \le r < n$):
- Number of even elements: $x = E[r+1] - E[l]$
- Number of odd elements: $y = O[r+1] - O[l]$

The valid condition $\frac{x}{y} \le \frac{a}{b}$ with $y > 0$ can be rewritten as:
$$b \cdot (E[r+1] - E[l]) \le a \cdot (O[r+1] - O[l])$$
$$b \cdot E[r+1] - a \cdot O[r+1] \le b \cdot E[l] - a \cdot O[l]$$

Let us define a transformed prefix value:
$$P[i] = b \cdot E[i] - a \cdot O[i]$$

The condition becomes:
$$P[r+1] \le P[l] \quad \text{for } 0 \le l < r+1 \le n$$

> **Note on $y > 0$ condition:**  
> If $O[r+1] - O[l] = 0$ (i.e. $y = 0$), then $E[r+1] - E[l] = r + 1 - l \ge 1$.  
> Hence, $P[r+1] - P[l] = b \cdot (E[r+1] - E[l]) \ge b \ge 1 > 0$.  
> Thus, $P[r+1] \le P[l]$ can never hold when $y = 0$. Therefore, $P[r+1] \le P[l]$ automatically guarantees $y > 0$.

#### Algorithm:
1. Compute the prefix transformed array $P$ of length $n + 1$, where $P[0] = 0$.
2. Coordinate compress the unique values of $P$.
3. Iterate $j$ from $0$ to $n$ and use a Binary Indexed Tree (Fenwick Tree) to query the count of previously seen indices $l < j$ where $P[l] \ge P[j]$.
4. Add this count to the answer and insert $P[j]$ into the Fenwick Tree.

### Complexity:
- **Time Complexity:** $\mathcal{O}(N \log N)$ due to sorting unique values for coordinate compression and performing $N+1$ Fenwick Tree operations.
- **Space Complexity:** $\mathcal{O}(N)$ for prefix arrays, coordinate compression mapping, and the Fenwick Tree.
