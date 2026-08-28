# 3734. Lexicographically Smallest Palindromic Permutation Greater Than Target

**Difficulty:** Hard

## Problem Description

You are given two strings `s` and `target`, each of length `n`, consisting of lowercase English letters.

Return the **lexicographically smallest** string that is both a **palindromic permutation** of `s` and **strictly greater** than `target`. If no such permutation exists, return an empty string `""`.

### Example 1:
**Input:** `s = "baba", target = "abba"`  
**Output:** `"baab"`  
**Explanation:** 
- The palindromic permutations of `s` (in lexicographical order) are `"abba"` and `"baab"`.
- The lexicographically smallest permutation that is strictly greater than `target` is `"baab"`.

### Example 2:
**Input:** `s = "baba", target = "bbaa"`  
**Output:** `""`  
**Explanation:** 
- The palindromic permutations of `s` (in lexicographical order) are `"abba"` and `"baab"`.
- None of them is lexicographically strictly greater than `target`. Therefore, the answer is `""`.

### Example 3:
**Input:** `s = "abc", target = "abb"`  
**Output:** `""`  
**Explanation:** 
- `s` has no palindromic permutations. Therefore, the answer is `""`.

### Example 4:
**Input:** `s = "aac", target = "abb"`  
**Output:** `"aca"`  
**Explanation:** 
- The only palindromic permutation of `s` is `"aca"`.
- `"aca"` is strictly greater than `target`. Therefore, the answer is `"aca"`.

### Constraints:
- `1 <= n == s.length == target.length <= 300`
- `s` and `target` consist of only lowercase English letters.

---

## Solution Approach

1. **Palindromic Feasibility:**
   - Count frequencies of all characters in `s`.
   - If more than one character has an odd frequency, no palindromic permutation can be formed from `s`. Return `""` immediately.
   - If there is an odd-count character, its odd instance must be the unique center character `mid_char` (for odd length $n$).
   - The available character pool for the first half of length $m = \lfloor n / 2 \rfloor$ is given by $\text{count}[c] // 2$ for each character $c$.

2. **Symmetry & Lexicographical Ordering:**
   - Any valid palindrome $P(L)$ is completely determined by its left half $L$:
     - $P(L) = L + L[::-1]$ (for even $n$)
     - $P(L) = L + \text{mid\_char} + L[::-1]$ (for odd $n$)
   - Since $P(L_1) < P(L_2) \iff L_1 < L_2$, minimizing $P(L)$ is equivalent to finding the lexicographically smallest left half $L$ such that $P(L) > \text{target}$.

3. **Two-Case Strategy:**
   - **Case 1: $L = \text{target}[:m]$:**
     - If the prefix $\text{target}[:m]$ can be formed exactly by the available left-half characters, we check whether $P(\text{target}[:m]) > \text{target}$.
     - If $P(\text{target}[:m]) > \text{target}$, this is unconditionally the minimal possible valid palindrome because any $L' < \text{target}[:m]$ would produce $P(L') < \text{target}$.
   - **Case 2: Finding Smallest $L > \text{target}[:m]$:**
     - Any $L > \text{target}[:m]$ guarantees $P(L) > \text{target}$ at the first mismatch index $i < m$.
     - We want $L$ to match $\text{target}[:m]$ on the longest possible prefix of length $i \in [0, m - 1]$ and then place the smallest available character $c > \text{target}[i]$ at position $i$.
     - Suffix $L[i+1:]$ is completed greedily by sorting the remaining available characters in ascending order.
     - Iterating $i$ downwards from the longest valid prefix of $\text{target}[:m]$ to $0$ ensures the first constructed candidate is the lexicographically smallest.

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N \cdot \Sigma)$ where $N$ is the length of the string and $\Sigma = 26$ is the alphabet size. Checking character availability and constructing strings takes linear time.
- **Space Complexity:** $\mathcal{O}(N)$ for character frequency maps and string reconstruction.
