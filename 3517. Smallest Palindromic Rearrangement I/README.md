# 3517. Smallest Palindromic Rearrangement I

**Difficulty:** Medium

## Problem Description

You are given a **palindromic** string `s`.

Return the **lexicographically smallest** palindromic **permutation** of `s`.

### Example 1:
**Input:** `s = "z"`  
**Output:** `"z"`  
**Explanation:** A string of only one character is already the lexicographically smallest palindrome.

### Example 2:
**Input:** `s = "babab"`  
**Output:** `"abbba"`  
**Explanation:** Rearranging `"babab"` -> `"abbba"` gives the smallest lexicographic palindrome.

### Example 3:
**Input:** `s = "daccad"`  
**Output:** `"acddca"`  
**Explanation:** Rearranging `"daccad"` -> `"acddca"` gives the smallest lexicographic palindrome.

### Constraints:
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.
- `s` is guaranteed to be palindromic.

## Solution Approach

1. **Symmetry Property:** Since `s` is guaranteed to be a palindrome, the first half `s[:n//2]` contains exactly one copy of every paired character present in `s`. If the length `n` is odd, `s[n//2]` is the center character.
2. **Lexicographical Order:** To make the palindrome lexicographically smallest, its left half (prefix of length `n//2`) must be as small as possible in lexicographical order.
3. **Sorting:** Sorting the characters of the left half `s[:n//2]` produces the smallest possible left half.
4. **Reconstruction:** 
   - If `n` is even: `result = sorted_half + sorted_half[::-1]`
   - If `n` is odd: `result = sorted_half + s[n//2] + sorted_half[::-1]`

### Complexity Analysis
- **Time Complexity:** $O(N \log N)$ where $N$ is the length of `s`, due to sorting the first half of length $N/2$. (Alternatively $O(N)$ with counting sort).
- **Space Complexity:** $O(N)$ auxiliary space for generating the result string.
