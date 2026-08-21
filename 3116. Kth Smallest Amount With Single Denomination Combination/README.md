# 3116. Kth Smallest Amount With Single Denomination Combination

**Difficulty:** Hard

## Problem Description

You are given an integer array `coins` representing coins of different denominations and an integer `k`.

You have an infinite number of coins of each denomination. However, you are **not allowed** to combine coins of different denominations.

Return the $k^{\text{th}}$ **smallest** amount that can be made using these coins.

---

### Example 1:

**Input:** `coins = [3,6,9], k = 3`  
**Output:** `9`  
**Explanation:**  
The given coins can make the following amounts:
- Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.
- Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.
- Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.  
All of the coins combined produce: 3, 6, **9**, 12, 15, etc.

### Example 2:

**Input:** `coins = [5,2], k = 7`  
**Output:** `12`  
**Explanation:**  
The given coins can make the following amounts:
- Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.
- Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.  
All of the coins combined produce: 2, 4, 5, 6, 8, 10, **12**, 14, 15, etc.

---

### Constraints:

- $1 \le \text{coins.length} \le 15$
- $1 \le \text{coins}[i] \le 25$
- $1 \le k \le 2 \times 10^9$
- `coins` contains pairwise distinct integers.

---

## Solution Approach

### 1. Monotonicity & Binary Search on Answer
The amounts that can be made by coin $c$ are its positive multiples ($c, 2c, 3c, \dots$). The set of all possible amounts is the union of multiples of all given coin denominations.
The count of generated amounts less than or equal to a value $X$ is a monotonically non-decreasing function $f(X)$.
Thus, we can binary search for the minimum $X$ such that $f(X) \ge k$.

- **Search Range:**
  - $\text{low} = 1$
  - $\text{high} = \min(\text{coins}) \times k \le 25 \times 2 \times 10^9 = 5 \times 10^{10}$.

### 2. Counting Multiples with Principle of Inclusion-Exclusion (PIE)
To evaluate $f(X)$, we need to find the number of integers in $[1, X]$ that are divisible by at least one coin in `coins`.
By the **Principle of Inclusion-Exclusion**:
$$f(X) = \sum_{S \subseteq \text{coins}, S \neq \emptyset} (-1)^{|S| - 1} \left\lfloor \frac{X}{\text{LCM}(S)} \right\rfloor$$

### 3. Redundancy Pruning
If a coin $c_j$ is divisible by another coin $c_i$ ($c_j \pmod{c_i} == 0$), every multiple of $c_j$ is already a multiple of $c_i$. Removing $c_j$ preserves the set of generated numbers while significantly reducing the number of subsets $2^n$.

### Complexity Analysis

- **Time Complexity:**
  - **Pruning & Subset Precomputation:** $O(n^2 + 2^n \cdot n)$ where $n \le 15$. $2^{15} = 32{,}768$ subsets.
  - **Binary Search:** $O(\log(\min(\text{coins}) \times k) \times 2^n) \approx 36 \times 2^n$ operations, executing in under $0.1$s in Python.
  - Overall Time: $\mathcal{O}(2^n \log(\min(\text{coins}) \cdot k))$.

- **Space Complexity:** $\mathcal{O}(2^n)$ to store precomputed LCM and signs of all subsets.
