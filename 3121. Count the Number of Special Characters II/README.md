# 3121. Count the Number of Special Characters II

**Difficulty:** Medium

## Problem Description

You are given a string `word`. A letter `c` is called **special** if it appears both in lowercase and uppercase in `word`, and **every** lowercase occurrence of `c` appears before the **first** uppercase occurrence of `c`.

Return *the number of **special** letters in* `word`.

### Example 1:
**Input:** `word = "aaAbcBC"`  
**Output:** `3`  
**Explanation:** The special characters are `'a'`, `'b'`, and `'c'`.

### Example 2:
**Input:** `word = "abc"`  
**Output:** `0`  
**Explanation:** There are no special characters in `word`.

### Example 3:
**Input:** `word = "abBCab"`  
**Output:** `0`  
**Explanation:** There are no special characters in `word`.

### Constraints:
- `1 <= word.length <= 2 * 10^5`
- `word` consists of only lowercase and uppercase English letters.

## Solution Approach

To satisfy the condition that every lowercase occurrence of a letter appears before the first uppercase occurrence, we need to track the position of these occurrences.

1.  **Index Tracking:** 
    - Use a dictionary or array to store the **last** index of each lowercase letter.
    - Use another dictionary or array to store the **first** index of each uppercase letter.
2.  **Iterate and Check:** 
    - For each letter from 'a' to 'z':
        - Check if it exists in both lowercase and uppercase sets.
        - If it does, verify if `last_lowercase_index < first_uppercase_index`.
3.  **Result:** Count the letters that meet these criteria.

### Complexity Analysis
- **Time Complexity:** $O(N)$, where $N$ is the length of the word, as we iterate through the string once to record indices and then 26 times to check conditions.
- **Space Complexity:** $O(1)$ since we only store indices for a fixed number of English letters (26 lowercase and 26 uppercase).
