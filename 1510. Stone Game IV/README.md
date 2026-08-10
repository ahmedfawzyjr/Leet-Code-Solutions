# 1510. Stone Game IV

**Difficulty:** Hard  
**Link:** [LeetCode](https://leetcode.com/problems/stone-game-iv/)

## Problem Description

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are `n` stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer `n`, return `true` if and only if Alice wins the game otherwise return `false`, assuming both players play optimally.

### Example 1:
**Input:** `n = 1`  
**Output:** `true`  
**Explanation:** Alice can remove 1 stone winning the game because Bob doesn't have any moves.

### Example 2:
**Input:** `n = 2`  
**Output:** `false`  
**Explanation:** Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).

### Example 3:
**Input:** `n = 4`  
**Output:** `true`  
**Explanation:** n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).

### Constraints:
- `1 <= n <= 10^5`

---

## Solution Analysis

### Dynamic Programming (Bottom-Up)

#### Intuition:
Let `dp[i]` be a boolean value representing whether the player whose turn it is can win the game with `i` stones remaining.

- A player will win from state `i` if there exists at least one valid move (removing `k * k` stones where `1 <= k * k <= i`) such that the remaining state `i - k * k` is a losing position for the opponent (`dp[i - k * k] == False`).
- If all reachable states `i - k * k` are winning positions for the opponent (`dp[i - k * k] == True`), then state `i` is a losing position (`dp[i] = False`).

#### Algorithm:
1. Initialize a boolean array `dp` of size `n + 1` with `False`.
2. For each `i` from 1 to `n`:
   - Iterate over all integers `j` such that `j * j <= i`.
   - If `not dp[i - j * j]`: set `dp[i] = True` and break early (since finding one winning transition is sufficient).
3. Return `dp[n]`.

#### Complexity Analysis:
- **Time Complexity:** $\mathcal{O}(n \sqrt{n})$ — For each number `i` up to `n`, we iterate up to $\sqrt{i}$ perfect squares. For $n = 10^5$, total iterations are around $\frac{2}{3} \cdot 10^5 \cdot \sqrt{10^5} \approx 2.1 \times 10^7$, which comfortably executes within time limits.
- **Space Complexity:** $\mathcal{O}(n)$ — For the 1D DP table of size `n + 1`.
