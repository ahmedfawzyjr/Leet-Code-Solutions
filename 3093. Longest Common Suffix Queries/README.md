# 3093. Longest Common Suffix Queries

**Difficulty:** Hard

## Problem Description

You are given two arrays of strings `wordsContainer` and `wordsQuery`.

For each `wordsQuery[i]`, you need to find a string from `wordsContainer` that has the **longest common suffix** with `wordsQuery[i]`. If there are two or more strings in `wordsContainer` that share the longest common suffix, find the string that is the **smallest in length**. If there are two or more such strings that have the same smallest length, find the one that occurred **earlier** in `wordsContainer`.

Return an array of integers `ans`, where `ans[i]` is the index of the string in `wordsContainer` that has the longest common suffix with `wordsQuery[i]`.

### Example 1:
**Input:** `wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]`  
**Output:** `[1,1,1]`  
**Explanation:**
- For `wordsQuery[0] = "cd"`, strings from `wordsContainer` sharing the longest common suffix "cd" are at indices 0, 1, and 2. Among these, index 1 is the answer because it has the shortest length (3).
- For `wordsQuery[1] = "bcd"`, strings from `wordsContainer` sharing the longest common suffix "bcd" are at indices 1 and 2. Index 1 is the answer because it has the shortest length (3).
- For `wordsQuery[2] = "xyz"`, no string shares a common suffix. Hence the string with the shortest length is chosen, which is at index 1.

### Example 2:
**Input:** `wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"]`  
**Output:** `[2,0,2]`  

### Constraints:
- `1 <= wordsContainer.length, wordsQuery.length <= 10^4`
- `1 <= wordsContainer[i].length <= 5 * 10^3`
- `1 <= wordsQuery[i].length <= 5 * 10^3`
- `wordsContainer[i]` and `wordsQuery[i]` consist only of lowercase English letters.
- Sum of `wordsContainer[i].length` is at most `5 * 10^5`.
- Sum of `wordsQuery[i].length` is at most `5 * 10^5`.

## Solution Approach

To efficiently find the longest common suffix, we can treat it as finding the **longest common prefix** by reversing all strings. A **Trie (Prefix Tree)** is the standard data structure for longest common prefix queries.

1.  **Reverse Strings:** Reverse every string in `wordsContainer` and `wordsQuery`.
2.  **Trie Construction:** 
    - Build a Trie using the reversed words from `wordsContainer`.
    - At each node of the Trie, store the `best_idx`. This index points to the string in `wordsContainer` that:
        - Passes through this node (shares this reversed prefix).
        - Has the smallest length among all such strings.
        - Has the smallest index in case of a length tie.
3.  **Handling Ties:** Before inserting any word, calculate the "global best" index (the shortest word in `wordsContainer`) and store it at the root. This covers cases where a query has no common suffix with any word in the container.
4.  **Query Processing:**
    - For each reversed query, traverse the Trie as far as possible.
    - The `best_idx` stored at the last reached node is the answer for that query.

### Complexity Analysis
- **Time Complexity:** $O(S_{container} + S_{query})$, where $S$ is the sum of lengths of all strings. Each character is processed a constant number of times.
- **Space Complexity:** $O(S_{container} \cdot \Sigma)$, where $\Sigma$ is the alphabet size (26). In the worst case, the Trie stores every character from `wordsContainer`.
