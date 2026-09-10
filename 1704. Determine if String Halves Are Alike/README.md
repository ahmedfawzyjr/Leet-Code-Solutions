# 1704. Determine if String Halves Are Alike

**Difficulty:** Easy  
**Topics:** String, Counting, Two Pointers  

## Problem Description

You are given a string `s` of even length. Split this string into two halves of equal lengths, and let `a` be the first half and `b` be the second half.

Two strings are **alike** if they have the same number of vowels (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`, `'A'`, `'E'`, `'I'`, `'O'`, `'U'`). Notice that `s` contains uppercase and lowercase letters.

Return `true` *if* `a` *and* `b` *are **alike***. Otherwise, return `false`.

---

### Example 1:

**Input:** `s = "book"`  
**Output:** `true`  
**Explanation:** `a = "bo"` and `b = "ok"`. `a` has 1 vowel and `b` has 1 vowel. Therefore, they are alike.

### Example 2:

**Input:** `s = "textbook"`  
**Output:** `false`  
**Explanation:** `a = "text"` and `b = "book"`. `a` has 1 vowel whereas `b` has 2. Therefore, they are not alike.  
Notice that the vowel `'o'` is counted twice.

---

### Constraints:

- $2 \le \text{s.length} \le 1000$
- `s.length` is even.
- `s` consists of uppercase and lowercase letters.

---

## Solution Approach

1. **Vowels Lookup Set:**
   - Define a set containing all lowercase and uppercase vowels: `{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}` for $\mathcal{O}(1)$ membership checking.

2. **Counting / Single Pass:**
   - Determine the midpoint $\text{mid} = \frac{\text{len}(s)}{2}$.
   - Iterate through indices from $0$ to $\text{mid} - 1$:
     - Increment a balance counter if the character at the left half $s[i]$ is a vowel.
     - Decrement the balance counter if the character at the right half $s[\text{mid} + i]$ is a vowel.
   - Return `true` if `balance == 0`, else `false`.

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the length of string `s`. We inspect each character of the string once.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space, since the vowel lookup set is of constant size ($10$ elements).
