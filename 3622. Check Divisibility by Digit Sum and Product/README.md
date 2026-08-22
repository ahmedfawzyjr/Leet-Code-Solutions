# 3622. Check Divisibility by Digit Sum and Product

**Difficulty:** Easy

## Problem Description

You are given a positive integer `n`. Determine whether `n` is divisible by the **sum** of the following two values:
- The **digit sum** of `n` (the sum of its digits).
- The **digit product** of `n` (the product of its digits).

Return `true` if `n` is divisible by this sum; otherwise, return `false`.

---

### Example 1:

**Input:** `n = 99`  
**Output:** `true`  
**Explanation:**  
Since 99 is divisible by the sum $(9 + 9 = 18)$ plus product $(9 \times 9 = 81)$ of its digits (total $18 + 81 = 99$), the output is `true`.

### Example 2:

**Input:** `n = 23`  
**Output:** `false`  
**Explanation:**  
Since 23 is not divisible by the sum $(2 + 3 = 5)$ plus product $(2 \times 3 = 6)$ of its digits (total $5 + 6 = 11$), the output is `false`.

---

### Constraints:

- $1 \le n \le 10^6$

---

## Solution Approach

1. **Extract Digits:** Extract each digit of $n$ using modulo $10$ (`n % 10`) and integer division (`n // 10`).
2. **Compute Values:**
   - **Digit Sum:** Accumulate the sum of all digits starting from 0.
   - **Digit Product:** Accumulate the product of all digits starting from 1.
3. **Divisibility Check:**
   - Compute $\text{total} = \text{digit\_sum} + \text{digit\_prod}$.
   - Check if $n \pmod{\text{total}} == 0$. Since $n \ge 1$, $\text{digit\_sum} \ge 1$ and $\text{digit\_prod} \ge 0$, guaranteeing $\text{total} \ge 1$ (no zero-division).
4. **Return Result:** Return `true` if divisible, otherwise `false`.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log_{10} n)$  
  The number of digits in $n$ is $\lfloor \log_{10} n \rfloor + 1$. For $n \le 10^6$, the loop executes at most 7 times, which runs in $\mathcal{O}(1)$ practical time.
  
- **Space Complexity:** $\mathcal{O}(1)$  
  Only a few integer variables are allocated to maintain the digit sum, digit product, and temporary values.
