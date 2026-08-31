# 1832. Check if the Sentence Is Pangram

**Difficulty:** Easy  
**Topics:** Hash Table, String

## Problem Description

A **pangram** is a sentence where every letter of the English alphabet appears at least once.

Given a string `sentence` containing only lowercase English letters, return `true` *if* `sentence` *is a **pangram**, or* `false` *otherwise*.

---

### Example 1:

**Input:** `sentence = "thequickbrownfoxjumpsoverthelazydog"`  
**Output:** `true`  
**Explanation:** `sentence` contains at least one of every letter of the English alphabet.

### Example 2:

**Input:** `sentence = "leetcode"`  
**Output:** `false`

---

### Constraints:

- $1 \le \text{sentence.length} \le 1000$
- `sentence` consists of lowercase English letters.

---

## Solution Approach

### Set / Hash Set Method

1. **Fast-path Length Check:**
   - The English alphabet has $26$ letters. If the length of `sentence` is less than $26$, it is impossible for `sentence` to contain all letters, so return `false` immediately.

2. **Distinct Character Counting:**
   - Convert the characters of `sentence` into a set (`set(sentence)`).
   - Check if the size of the set equals $26$.
   - Since `sentence` is guaranteed to contain only lowercase English letters, having $26$ distinct elements guarantees every letter from `'a'` to `'z'` is present.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the length of `sentence`. We scan the string once to populate the set.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space (or $\mathcal{O}(\Sigma)$ where $\Sigma = 26$ is the fixed size of the English alphabet).
