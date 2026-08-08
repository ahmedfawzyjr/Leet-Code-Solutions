# 3302. Find the Lexicographically Smallest Valid Sequence

**Difficulty:** Medium

## Problem Description

You are given two strings `word1` and `word2`.

A string `x` is called **almost equal** to `y` if you can change **at most one character** in `x` to make it **identical** to `y`.

A sequence of indices `seq` is called **valid** if:
- The indices are sorted in **ascending order**.
- Concatenating the characters at these indices in `word1` in the **same** order results in a string that is **almost equal** to `word2`.

Return an array of size `word2.length` representing the **lexicographically smallest** valid sequence of indices. If no such sequence of indices exists, return an empty array.

**Note** that the answer must represent the *lexicographically smallest array*, not the corresponding string formed by those indices.

### Example 1:
**Input:** `word1 = "vbcca", word2 = "abc"`  
**Output:** `[0,1,2]`  
**Explanation:**  
The lexicographically smallest valid sequence of indices is `[0, 1, 2]`:
- Change `word1[0]` to `'a'`.
- `word1[1]` is already `'b'`.
- `word1[2]` is already `'c'`.

### Example 2:
**Input:** `word1 = "bacdc", word2 = "abc"`  
**Output:** `[1,2,4]`  
**Explanation:**  
The lexicographically smallest valid sequence of indices is `[1, 2, 4]`:
- `word1[1]` is already `'a'`.
- Change `word1[2]` to `'b'`.
- `word1[4]` is already `'c'`.

### Example 3:
**Input:** `word1 = "aaaaaa", word2 = "aaabc"`  
**Output:** `[]`  
**Explanation:**  
There is no valid sequence of indices.

### Example 4:
**Input:** `word1 = "abc", word2 = "ab"`  
**Output:** `[0,1]`  

### Constraints:
- `1 <= word2.length <= word1.length <= 3 * 10^5`
- `word1` and `word2` consist only of lowercase English letters.

## Solution Approach

We want to find the lexicographically smallest sequence of indices `seq` in `word1` of length `m = len(word2)` such that the subsequence formed by `seq` matches `word2` with at most 1 mismatch.

### Key Insights:
1. **Right-to-Left Precomputation (`last` array):**
   - Precompute `last[j]`, which is the maximum index in `word1` where `word2[j]` can be matched if we greedily match the suffix `word2[j..m-1]` from right to left in `word1` with **0 mismatches**.
   - If `word2[j..m-1]` cannot be matched in `word1` with 0 mismatches, `last[j] = -1`.

2. **Greedy Left-to-Right Matching:**
   - To make the index sequence lexicographically smallest, at each step `j` (from `0` to `m-1`), we pick the smallest possible index `i > prev_i` in `word1` that allows us to validly complete the remainder of `word2`.
   - We track whether we have already consumed our 1 allowed mismatch (`used_mismatch`).

3. **Validity Conditions for Candidate Index `i`:**
   - **If `word1[i] == word2[j]`:**
     - If `used_mismatch` is `False`: Valid if `j == m - 1`, `last[j+1] > i`, `j == m - 2`, or `last[j+2] > i + 1`. (The last two handle the case where the 1 mismatch occurs at `word2[j+1]`).
     - If `used_mismatch` is `True`: Valid if `j == m - 1` or `last[j+1] > i`.
   - **If `word1[i] != word2[j]`:**
     - Requires `not used_mismatch`. Valid if `j == m - 1` or `last[j+1] > i`. This consumes the 1 allowed mismatch.

### Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N + M)$, where $N = \text{len}(word1)$ and $M = \text{len}(word2)$. Precomputing `last` takes $\mathcal{O}(N)$ time, and the outer loop over `j` advances `i` monotonically from `0` to `N-1`, taking $\mathcal{O}(N + M)$ overall.
- **Space Complexity:** $\mathcal{O}(M)$ for storing `last` array and the resulting sequence of indices.
