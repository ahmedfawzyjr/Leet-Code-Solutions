# 3718. Smallest Missing Multiple of K

**Difficulty:** Easy  
**Topics:** Array, Hash Table, Math

## Problem Description

Given an integer array `nums` and an integer `k`, return the **smallest positive multiple** of `k` that is **missing** from `nums`.

A **multiple** of `k` is any positive integer divisible by `k`.

---

### Example 1:

**Input:** `nums = [8, 2, 3, 4, 6]`, `k = 2`  
**Output:** `10`  
**Explanation:**  
The multiples of $k = 2$ are $2, 4, 6, 8, 10, 12\dots$ and the smallest multiple missing from `nums` is $10$.

### Example 2:

**Input:** `nums = [1, 4, 7, 10, 15]`, `k = 5`  
**Output:** `5`  
**Explanation:**  
The multiples of $k = 5$ are $5, 10, 15, 20\dots$ and the smallest multiple missing from `nums` is $5$.

---

### Constraints:

- $1 \le \text{nums.length} \le 100$
- $1 \le \text{nums}[i] \le 100$
- $1 \le k \le 100$

---

## Solution Approach

1. **Hash Set Conversion:**
   - Convert the array `nums` into a hash set `num_set` to achieve $\mathcal{O}(1)$ average-time lookup.

2. **Sequential Multiple Check:**
   - Start with the first positive multiple of $k$, which is `multiple = k`.
   - Repeatedly increment `multiple` by $k$ (`multiple += k`) as long as `multiple` is contained in `num_set`.

3. **Return Smallest Missing:**
   - Once a multiple is found that does not exist in `num_set`, return it immediately.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$  
  Converting `nums` to a hash set takes $\mathcal{O}(N)$ time, where $N$ is the number of elements in `nums`. In the worst case, `nums` contains the first $N$ multiples of $k$, requiring $N + 1$ set lookups before reaching the missing multiple. Hence, the overall time complexity is $\mathcal{O}(N)$.

- **Space Complexity:** $\mathcal{O}(N)$  
  A hash set of size at most $N$ is maintained for quick element existence checks.
