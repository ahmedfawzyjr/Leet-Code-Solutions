# 1927. Sum Game

**Difficulty:** Medium  
**Topics:** Math, String, Greedy, Game Theory

## Problem Description

Alice and Bob take turns playing a game, with **Alice starting first**.

You are given a string `num` of **even length** consisting of digits and `'?'` characters. On each turn, a player will do the following if there is still at least one `'?'` in `num`:
1. Choose an index `i` where `num[i] == '?'`.
2. Replace `num[i]` with any digit between `'0'` and `'9'`.

The game ends when there are no more `'?'` characters in `num`.

For **Bob to win**, the sum of the digits in the first half of `num` must be **equal** to the sum of the digits in the second half. For **Alice to win**, the sums must **not be equal**.

- For example, if the game ended with `num = "243801"`, then Bob wins because $2 + 4 + 3 = 9 = 8 + 0 + 1$. If the game ended with `num = "243803"`, then Alice wins because $2 + 4 + 3 = 9 \ne 8 + 0 + 3 = 11$.

Assuming Alice and Bob play optimally, return `true` *if Alice will win and* `false` *if Bob will win*.

---

### Example 1:

**Input:** `num = "5023"`  
**Output:** `false`  
**Explanation:**  
There are no moves to be made.  
The sum of the first half is equal to the sum of the second half: $5 + 0 = 2 + 3 = 5$.

### Example 2:

**Input:** `num = "25??"`  
**Output:** `true`  
**Explanation:**  
Alice can replace one of the `'?'`s with `'9'` and it will be impossible for Bob to make the sums equal.

### Example 3:

**Input:** `num = "?3295???"`  
**Output:** `false`  
**Explanation:**  
It can be proven that Bob will always win. One possible outcome is:
- Alice replaces the first `'?'` with `'9'`. `num = "93295???"`.
- Bob replaces one of the `'?'` in the right half with `'9'`. `num = "932959??"`.
- Alice replaces one of the `'?'` in the right half with `'2'`. `num = "9329592?"`.
- Bob replaces the last `'?'` in the right half with `'7'`. `num = "93295927"`.
Bob wins because $9 + 3 + 2 + 9 = 23 = 5 + 9 + 2 + 7$.

---

### Constraints:

- $2 \le \text{num.length} \le 10^5$
- `num.length` is **even**.
- `num` consists of only digits and `'?'`.

---

## Solution Approach

Let:
- $S_1$ = sum of initial digits in the left half ($0 \le i < n/2$)
- $S_2$ = sum of initial digits in the right half ($n/2 \le i < n$)
- $C_1$ = count of `'?'` in the left half
- $C_2$ = count of `'?'` in the right half

### 1. Odd Total Question Marks ($C_1 + C_2$ is odd)
- Alice gets more turns than Bob and will make the very last move.
- Right before Alice's final move, exactly one `'?'` remains.
- To make the sums equal, there is at most **one** digit $d \in [0, 9]$ that would balance the two halves.
- Alice wants the sums to be unequal, so she can simply pick any of the other 9 digits.
- Therefore, **Alice is guaranteed to win**.

### 2. Even Total Question Marks ($C_1 + C_2$ is even)
- Bob makes the last move.
- For the $\min(C_1, C_2)$ question marks on both sides, Bob can use a **mirroring strategy**: whenever Alice plays digit $d$ on one side, Bob plays $d$ on the opposing side, perfectly cancelling out any difference.
- For the excess $k = |C_1 - C_2|$ question marks on the side with more `'?'`:
  - There are $k / 2$ pairs of moves $(Alice, Bob)$ played on that side.
  - For each pair, if Alice chooses $d$, Bob can respond with $9 - d$, guaranteeing that each pair of moves contributes exactly $d + (9 - d) = 9$ to that side.
  - If Bob needs anything other than 9 per pair, Alice can foil him by playing 0 or 9.
  - Thus, Bob can only ensure the excess question marks contribute $\frac{k}{2} \times 9 = \frac{|C_1 - C_2|}{2} \times 9$.

### Unified Winning Condition
Bob wins if and only if:
$$(S_1 - S_2) = \frac{C_2 - C_1}{2} \times 9 \iff 2 \times (S_1 - S_2) = 9 \times (C_2 - C_1)$$

Alice wins whenever this equality **does not hold** (or when $C_1 + C_2$ is odd, which is also naturally handled since $2 \times (S_1 - S_2)$ is even while $9 \times (C_2 - C_1)$ is odd).

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$ — Single pass over the string of length $n$ to compute sums and count `'?'`.
- **Space Complexity:** $\mathcal{O}(1)$ — Constant auxiliary space used for sum and count variables.
