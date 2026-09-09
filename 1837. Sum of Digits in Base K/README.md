# 1837. Sum of Digits in Base K

**Difficulty:** Easy  
**Topics:** Math

## Problem Description

Given an integer `n` (in base `10`) and a base `k`, return the *sum of the digits of* `n` *after converting* `n` *from base* `10` *to base* `k`.

After converting, each digit should be interpreted as a base `10` number, and the sum should be returned in base `10`.

---

### Example 1:

**Input:** `n = 34, k = 6`  
**Output:** `9`  
**Explanation:** `34` (base `10`) expressed in base `6` is `54`. `5 + 4 = 9`.

### Example 2:

**Input:** `n = 10, k = 10`  
**Output:** `1`  
**Explanation:** `n` is already in base `10`. `1 + 0 = 1`.

---

### Constraints:

- $1 \le n \le 100$
- $2 \le k \le 10$

---

## Solution Approach

### Base Conversion & Digit Sum Extraction

1. **Repeated Division:**
   - To find the digits of `n` in base `k`, repeatedly take the remainder of `n` when divided by `k` (`n % k`). Each remainder represents a digit in base `k`.
   - Add this remainder to an accumulating sum `total`.
   - Update `n` by integer division by `k` (`n //= k`).

2. **Termination:**
   - Continue the process until `n` becomes `0`.
   - Return `total`.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log_k n)$. The number of iterations is bounded by the number of digits of $n$ in base $k$, which is at most $\lfloor \log_k n \rfloor + 1 \le 7$ operations for $n \le 100$.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space as we only use a simple loop and integer counters.
