# 3120. Count the Number of Special Characters I

**Difficulty:** Easy

## Problem Description

You are given a string `word`. A letter is called **special** if it appears both in lowercase and uppercase in `word`.

Return *the number of **special** letters in* `word`.

### Example 1:
**Input:** `word = "aaAbcBC"`  
**Output:** `3`  
**Explanation:** The special characters in `word` are `'a'`, `'b'`, and `'c'`.

### Example 2:
**Input:** `word = "abc"`  
**Output:** `0`  
**Explanation:** No character in `word` appears in uppercase.

### Example 3:
**Input:** `word = "abBCab"`  
**Output:** `1`  
**Explanation:** The only special character in `word` is `'b'`.

### Constraints:
- `1 <= word.length <= 50`
- `word` consists of only lowercase and uppercase English letters.

## Solution Approach

We can use a hash set to store all the unique characters present in the string for $O(1)$ lookups. Then, we iterate through the English alphabet and check if both the lowercase and uppercase versions of each letter are present in the set.

1.  **Unique Characters:** Convert the input string into a set of characters.
2.  **Alphabet Iteration:** For each letter from 'a' to 'z':
    - Check if the lowercase version (e.g., 'a') is in the set.
    - Check if the uppercase version (e.g., 'A') is in the set.
    - If both are present, increment the special character count.
3.  **Result:** Return the final count.

### Complexity Analysis
- **Time Complexity:** $O(N)$, where $N$ is the length of the word, to create the set. The alphabet check is $O(26) = O(1)$.
- **Space Complexity:** $O(1)$ as the set will store at most 52 unique English characters.
