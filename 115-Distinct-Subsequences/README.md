# 115. Distinct Subsequences

**Difficulty:** Hard  
**Topics:** String, Dynamic Programming

## Problem Description

Given two strings `s` and `t`, return *the number of distinct* ***subsequences*** *of* `s` *which equals* `t`.

The test cases are generated so that the answer fits on a 32-bit signed integer.

---

### Example 1:

**Input:** `s = "rabbbit", t = "rabbit"`  
**Output:** `3`  
**Explanation:**  
As shown below, there are 3 ways you can generate "rabbit" from `s`.  
`rabb_bit`  
`rab_bbit`  
`ra_bbbit`

```
rabbbit
^^^^ ^^ (rabb bit -> rabbit)
^^^ ^^^ (rab bbit -> rabbit)
^^ ^^^^ (ra bbbit -> rabbit)
```

### Example 2:

**Input:** `s = "babgbag", t = "bag"`  
**Output:** `5`  
**Explanation:**  
As shown below, there are 5 ways you can generate "bag" from `s`.  
`ba_g___`  
`ba____g`  
`b__g_a_`  
`__bg_a_`  
`___gbag`

---

### Constraints:

- $1 \le \text{s.length}, \text{t.length} \le 1000$
- `s` and `t` consist of English letters.

---

## Solution Approach

### Dynamic Programming (1D Space Optimized)

We want to find the number of subsequences of `s` that form the target string `t`.

1. **State Definition:**
   - Let `dp[j]` be the number of distinct subsequences of `s[:i]` that equal `t[:j]`.

2. **Base Case:**
   - `dp[0] = 1`: An empty string `t` can always be formed by deleting all characters in `s`, which corresponds to exactly 1 distinct empty subsequence.
   - For all $j > 0$, `dp[j] = 0` initially.

3. **Transitions:**
   - For each character `s[i-1]` in `s` (from $i = 1$ to $m$):
     - Iterate backwards over $j$ from $n$ down to $1$:
       - If `s[i-1] == t[j-1]`:
         $$\text{dp}[j] = \text{dp}[j] + \text{dp}[j-1]$$
         - `dp[j]` represents ignoring the current character `s[i-1]` (matching `t[:j]` using only previous characters in `s`).
         - `dp[j-1]` represents matching `s[i-1]` with `t[j-1]` (and matching `t[:j-1]` with previous characters in `s`).
       - If `s[i-1] != t[j-1]`:
         - `dp[j]` remains unchanged (we cannot match `s[i-1]` with `t[j-1]`).

4. **Space Optimization:**
   - Iterating $j$ backwards from $n$ down to $1$ allows us to use a single 1D array of size $n + 1$ without overwriting values needed for the current step.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(m \cdot n)$, where $m = \text{len}(s)$ and $n = \text{len}(t)$. We iterate over all characters of `s` and update up to $n$ states in the inner loop.
- **Space Complexity:** $\mathcal{O}(n)$ auxiliary space for the 1D DP array of size $n + 1$.
