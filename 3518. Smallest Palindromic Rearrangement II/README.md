# 3518. Smallest Palindromic Rearrangement II

**Difficulty:** Hard

## Problem Description

You are given a **palindromic** string `s` and an integer `k`.

Return the `k`-th **lexicographically smallest** palindromic **permutation** of `s`. If there are fewer than `k` distinct palindromic permutations, return an empty string.

Note: Different rearrangements that yield the same palindromic string are considered identical and are counted once.

### Example 1:
**Input:** `s = "abba", k = 2`  
**Output:** `"baab"`  
**Explanation:** 
- The two distinct palindromic rearrangements of `"abba"` are `"abba"` and `"baab"`.
- Lexicographically, `"abba"` comes before `"baab"`. Since `k = 2`, the output is `"baab"`.

### Example 2:
**Input:** `s = "aa", k = 2`  
**Output:** `""`  
**Explanation:** 
- There is only one palindromic rearrangement: `"aa"`.
- The output is empty string since `k = 2` exceeds the number of possible rearrangements.

### Example 3:
**Input:** `s = "bacab", k = 1`  
**Output:** `"abcba"`  
**Explanation:** 
- The two distinct palindromic rearrangements of `"bacab"` are `"abcba"` and `"bacab"`.
- Lexicographically, `"abcba"` comes before `"bacab"`. Since `k = 1`, the output is `"abcba"`.

### Constraints:
- `1 <= s.length <= 10^4`
- `s` consists of lowercase English letters.
- `s` is guaranteed to be palindromic.
- `1 <= k <= 10^9`

## Solution Approach

1. **Symmetry Property:** Since any palindromic permutation is symmetric, it is uniquely determined by its first half (left half) of length $m = \text{len}(s) // 2$. The middle character (if the length is odd) is uniquely determined as the character with the odd count in `s`.
2. **Lexicographical Correspondence:** The lexicographical order of two palindromes $P_1 < P_2$ is equivalent to the lexicographical order of their first halves $p_1 < p_2$. Thus, the problem reduces to finding the $k$-th lexicographically smallest permutation of the multiset of characters in the first half.
3. **Digit-by-Digit Construction:**
   - Compute the character counts for the left half. Let $m$ be the total length of the left half.
   - Calculate the total number of permutations of these characters:
     $$ W = \frac{m!}{\prod (count[x]!)} $$
   - If $k > W$, return `""` immediately.
   - Iterate position by position from $0$ to $m - 1$:
     - For each possible character $x \in \{'a', \dots, 'z'\}$ in alphabetical order:
       - If $x$ is available, calculate the number of permutations if $x$ is placed at the current position:
         $$ \text{ways} = \frac{W \times count[x]}{R} $$
         where $R$ is the remaining length.
       - If $k > \text{ways}$, we subtract $\text{ways}$ from $k$ and try the next character.
       - Otherwise, we place $x$, decrement its count, update the total ways $W \leftarrow \text{ways}$, and proceed to the next position.
4. **Reconstruction:** Construct the final palindrome using the constructed left half, the middle character (if odd length), and the reversed left half.

### Complexity Analysis
- **Time Complexity:** $O(N \cdot \Sigma)$ where $N$ is the length of `s` and $\Sigma = 26$ is the alphabet size. Since Python handles arbitrarily large integer arithmetic efficiently, the factorial division step is extremely fast.
- **Space Complexity:** $O(N)$ for storing counts and constructing the result.
