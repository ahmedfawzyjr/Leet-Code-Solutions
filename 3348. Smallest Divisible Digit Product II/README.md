# 3348. Smallest Divisible Digit Product II

**Difficulty:** Hard

## Problem Description

You are given a string `num` which represents a **positive integer**, and an integer `t`.

A number is called **zero-free** if none of its digits are 0.

Return a string representing the **smallest zero-free** number greater than or equal to `num` such that the **product of its digits is divisible by `t`**. If no such number exists, return `"-1"`.

### Example 1:
**Input:** `num = "1234", t = 256`  
**Output:** `"1488"`  
**Explanation:** The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.

### Example 2:
**Input:** `num = "12355", t = 50`  
**Output:** `"12355"`  
**Explanation:** 12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.

### Example 3:
**Input:** `num = "11111", t = 26`  
**Output:** `"-1"`  
**Explanation:** No number greater than 11111 has the product of its digits divisible by 26.

### Constraints:
- $2 \le \text{num.length} \le 2 \times 10^5$
- `num` consists only of digits in the range `['0', '9']`.
- `num` does not contain leading zeros.
- $1 \le t \le 10^{14}$

---

## Solution Approach

### 1. Prime Factorization
Digits $1..9$ can only contribute prime factors $2, 3, 5,$ and $7$.
- First, factorize $t = 2^{c_2} \cdot 3^{c_3} \cdot 5^{c_5} \cdot 7^{c_7}$.
- If $t$ has any prime factor other than $2, 3, 5, 7$, it is impossible to form a valid digit product, so return `"-1"`.

### 2. Greedy Digit Count Calculation (`min_digits`)
To check whether remaining required factor counts $(c_2, c_3, c_5, c_7)$ can fit in $K$ digits:
- $c_7$ sevens require $c_7$ digits of `'7'`.
- $c_5$ fives require $c_5$ digits of `'5'`.
- For $c_3$ threes: maximum per digit is `'9'` ($3^2$), so we use $\lfloor c_3 / 2 \rfloor$ nines, leaving $rem_3 \in \{0, 1\}$.
- For $c_2$ twos: maximum per digit is `'8'` ($2^3$), so we use $\lfloor c_2 / 3 \rfloor$ eights, leaving $rem_2 \in \{0, 1, 2\}$.
- If $rem_3 = 1$ and $rem_2 = 1$, combine them into a single `'6'` ($2^1 \cdot 3^1$).
- Otherwise, add $rem_3$ digits for $3$ and $1$ digit if $rem_2 > 0$.

### 3. Digit Placement (Greedy + Backtracking Matching)
We evaluate two cases:

- **Case 1: Same Length $N$**
  - Check if `num` itself is zero-free and valid.
  - Otherwise, find the longest matching prefix `num[0...i-1]` (up to the first `'0'` in `num`).
  - At position $i$, try digits $d > \text{num}[i]$. If remaining length $N - 1 - i$ can satisfy factor requirements, build the rest of the suffix greedily left-to-right (choosing the smallest valid digit at each step).

- **Case 2: Larger Length $> N$**
  - Set target length $L = \max(N + 1, \text{min\_digits}(c_2, c_3, c_5, c_7))$.
  - Construct a string of length $L$ greedily from left to right.

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the length of `num`. Checking prefix positions and filling the suffix takes $O(1)$ operations per digit.
- **Space Complexity:** $\mathcal{O}(N)$ to construct and return the result string.
