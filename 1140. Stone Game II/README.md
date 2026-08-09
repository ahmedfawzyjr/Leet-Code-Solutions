# 1140. Stone Game II

**Difficulty:** Medium  
**Link:** [LeetCode](https://leetcode.com/problems/stone-game-ii/)

## Problem Description

Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones `piles[i]`. The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.

On each player's turn, that player can take **all the stones** in the first $X$ remaining piles, where $1 \le X \le 2M$. Then, we set $M = \max(M, X)$. Initially, $M = 1$.

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

### Example 1:
**Input:** `piles = [2,7,9,4,4]`  
**Output:** `10`  
**Explanation:**  
- If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get $2 + 4 + 4 = 10$ stones in total.  
- If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get $2 + 7 = 9$ stones in total.  
So we return 10 since it's larger.

### Example 2:
**Input:** `piles = [1,2,3,4,5,100]`  
**Output:** `104`

### Constraints:
- `1 <= piles.length <= 100`
- `1 <= piles[i] <= 10^4`

---

## Solution Analysis

### Dynamic Programming with Memoization (Minimax / Game Theory)

#### Intuition:
Let `dp(i, M)` represent the maximum number of stones the *current player* can collect starting from index `i` with parameter `M`.

At index `i`, total stones remaining in the game is $\text{suffix\_sum}[i] = \sum_{k=i}^{N-1} \text{piles}[k]$.

If the current player decides to pick $X$ piles ($1 \le X \le 2M$):
- The remaining stones from index $i + X$ with parameter $\max(M, X)$ will be played optimally by the opponent.
- The opponent will receive `dp(i + X, max(M, X))` stones.
- Therefore, the current player will receive $\text{suffix\_sum}[i] - \text{dp}(i + X, \max(M, X))$ stones.

The current player wants to maximize their score:
$$\text{dp}(i, M) = \max_{1 \le X \le 2M} \left( \text{suffix\_sum}[i] - \text{dp}(i + X, \max(M, X)) \right)$$

#### Base Case:
If $i + 2M \ge N$, the current player can take all remaining piles at once ($X = N - i$), collecting $\text{suffix\_sum}[i]$ stones.

#### Complexity Analysis:
- **Time Complexity:** $\mathcal{O}(N^3)$ — Total states are $\mathcal{O}(N^2)$ since $i \le N$ and $M \le N$. For each state, we iterate $X$ up to $2M \le 2N$. With $N \le 100$, maximum operations are around $\frac{N^3}{3} \approx 3 \times 10^5$, which executes in a few milliseconds.
- **Space Complexity:** $\mathcal{O}(N^2)$ — For the memoization table storing states $(i, M)$ and recursion call stack.
