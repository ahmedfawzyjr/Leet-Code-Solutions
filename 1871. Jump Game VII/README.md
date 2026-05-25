# 1871. Jump Game VII

**Difficulty:** Medium

## Problem Description

You are given a **0-indexed** binary string `s` and two integers `minJump` and `maxJump`. In the beginning, you are standing at index `0`, which is equal to `'0'`. You can move from index `i` to index `j` if the following conditions are fulfilled:

- `i + minJump <= j <= min(i + maxJump, s.length - 1)`, and
- `s[j] == '0'`.

Return `true` *if you can reach index* `s.length - 1` *in* `s`, *or* `false` *otherwise*.

### Example 1:
**Input:** `s = "011010", minJump = 2, maxJump = 3`  
**Output:** `true`  
**Explanation:**
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.

### Example 2:
**Input:** `s = "01101110", minJump = 2, maxJump = 3`  
**Output:** `false`

### Constraints:
- `2 <= s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`.
- `s[0] == '0'`.
- `1 <= minJump <= maxJump < s.length`.

## Solution Approach

This problem can be solved using **Dynamic Programming** with a **Sliding Window** optimization to handle the range condition efficiently.

1.  **DP State:** Let `dp[i]` be a boolean indicating whether index `i` is reachable from index `0`.
2.  **Transitions:** Index `j` is reachable if `s[j] == '0'` and there exists an index `i` such that `dp[i]` is true and `j - maxJump <= i <= j - minJump`.
3.  **Optimization:** Instead of checking all `i` in the range for every `j` (which would be $O(N \cdot maxJump)$), we maintain a running count (`reachable_count`) of how many `true` values exist in the current window `[j - maxJump, j - minJump]`.
    - As `j` increases, we add `dp[j - minJump]` to the count and remove `dp[j - maxJump - 1]` from the count.
4.  **Result:** The answer is `dp[n-1]`.

### Complexity Analysis
- **Time Complexity:** $O(N)$, where $N$ is the length of the string `s`, as we iterate through the string once.
- **Space Complexity:** $O(N)$ to store the `dp` array.
