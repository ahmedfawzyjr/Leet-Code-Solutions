# 3797. Count Routes to Climb a Rectangular Grid

**Difficulty**: Hard

## Problem Description

You are given a string array `grid` of size `m`, where each string `grid[i]` has length `n`. The character `grid[i][j]` is one of the following symbols:
- `'.'`: The cell is available.
- `'#'`: The cell is blocked.

You want to count the number of different routes to climb `grid`. Each route must start from any cell in the bottom row (row $m - 1$) and end in the top row (row $0$).

However, there are some constraints on the route:
- You can only move from one available cell to **another** available cell.
- The **Euclidean distance** of each move is **at most** $d$, where $d$ is an integer parameter given to you. The Euclidean distance between two cells $(r1, c1)$ and $(r2, c2)$ is $\sqrt{(r1 - r2)^2 + (c1 - c2)^2}$.
- Each move either stays on the same row or moves to the row directly above (from row $r$ to $r - 1$).
- You **cannot stay on the same row for two consecutive turns**. If you stay on the same row in a move (and this move is not the last move), your next move must go to the row above.

Return an integer denoting the number of such routes. Since the answer may be very large, return it **modulo** $10^9 + 7$.

---

## Examples

### Example 1

**Input**: `grid = ["..", "#."]`, `d = 1`  
**Output**: `2`  
**Explanation**:  
We label the cells we visit in the routes sequentially, starting from 1. The two routes are:
```
.2
#1
```
and
```
22
#1
```
We can move from the cell $(1, 1)$ to $(0, 1)$ because the Euclidean distance is $\sqrt{(1 - 0)^2 + (1 - 1)^2} = \sqrt{1} \le d$.  
However, we cannot move from the cell $(1, 1)$ to the cell $(0, 0)$ because the Euclidean distance is $\sqrt{(1 - 0)^2 + (1 - 0)^2} = \sqrt{2} > d$.

### Example 2

**Input**: `grid = ["..", "#."]`, `d = 2`  
**Output**: `4`  
**Explanation**:  
Two of the routes are given in Example 1. The other two routes are:
```
2.
#1
```
and
```
23
#1
```
Note that we can move from $(1, 1)$ to $(0, 0)$ because the Euclidean distance is $\sqrt{2} \le d$.

### Example 3

**Input**: `grid = ["#"]`, `d = 750`  
**Output**: `0`  
**Explanation**:  
We cannot choose any cell as the starting cell. Therefore, there are no routes.

### Example 4

**Input**: `grid = [".."]`, `d = 1`  
**Output**: `4`  
**Explanation**:  
The possible routes are:
- `.1`
- `1.`
- `12`
- `21`

---

## Constraints

- $1 \le m == \text{grid.length} \le 750$
- $1 \le n == \text{grid}[i]\text{.length} \le 750$
- `grid[i][j]` is `'.'` or `'#'`.
- $1 \le d \le 750$

---

## Solution Approach

### Dynamic Programming with Prefix Sum Optimization

1. **State Constraints & Transitions**:
   - In each row $r$, a route can visit either:
     - Just 1 cell: entered directly from row $r + 1$ (or initialized here if $r = m - 1$), and next step moves to row $r - 1$.
     - 2 cells: entered at $(r, c_1)$ from row $r + 1$, moves horizontally to $(r, c_2)$ ($c_1 \neq c_2$, $|c_1 - c_2| \le d$), and next step moves to row $r - 1$.
   - Note that because we cannot make two consecutive horizontal moves, at most **one** horizontal move is allowed per row visit.

2. **DP Formulation**:
   - Let $\text{dp\_from\_below}[c]$ denote the number of valid path prefixes that arrive at $(r, c)$ via a row transition from row $r + 1$ (or start at $(m - 1, c)$).
   - In row $r$:
     - A route may either leave immediately from $(r, c)$, contributing $\text{dp\_from\_below}[c]$ routes ending at $(r, c)$ before moving up.
     - Or it could make a horizontal step from some $(r, k)$ ($k \neq c$) with $|k - c| \le d$. The number of ways to reach $(r, c)$ via horizontal move is $\sum_{k \neq c, |k - c| \le d} \text{dp\_from\_below}[k]$.
     - Therefore:
       $$\text{dp\_current\_cell}[c] = \text{dp\_from\_below}[c] + \sum_{\substack{k \neq c \\ |k - c| \le d}} \text{dp\_from\_below}[k]$$
       We can compute the range sum $\sum_{|k - c| \le d} \text{dp\_from\_below}[k]$ in $O(1)$ time using standard prefix sums.
   - Moving from row $r$ to row $r - 1$:
     - For a transition from $(r, c)$ to $(r - 1, c_{\text{up}})$, the Euclidean distance condition requires:
       $$\sqrt{(r - (r - 1))^2 + (c - c_{\text{up}})^2} \le d \iff 1 + (c - c_{\text{up}})^2 \le d^2 \iff |c - c_{\text{up}}| \le \lfloor\sqrt{d^2 - 1}\rfloor$$
     - Let $d_{\text{col\_max}} = \lfloor\sqrt{d^2 - 1}\rfloor$.
     - Then for $(r - 1, c_{\text{up}})$:
       $$\text{next\_dp\_from\_below}[c_{\text{up}}] = \sum_{|c - c_{\text{up}}| \le d_{\text{col\_max}}} \text{dp\_current\_cell}[c]$$
       which is also computed in $O(1)$ per cell using prefix sums of $\text{dp\_current\_cell}$.

3. **Base Case & Final Answer**:
   - Initialize $\text{dp\_from\_below}[c] = 1$ for all available cells `grid[m - 1][c] == '.'` at row $m - 1$.
   - Iterate row by row from $m - 1$ up to $0$.
   - At row $0$, after computing $\text{dp\_current\_cell}$, the total number of valid routes is $\sum_{c=0}^{n-1} \text{dp\_current\_cell}[c] \pmod{10^9 + 7}$.

### Complexity Analysis
- **Time Complexity**: $O(m \times n)$ because for each cell we perform $O(1)$ range sum queries via prefix sums.
- **Space Complexity**: $O(n)$ space since we only need the DP arrays and prefix sum arrays for the current and previous row.

---

## Python Code

```python
import math
from typing import List

class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7
        
        # dp_from_below[c]: number of valid routes that reach (r, c) by a vertical step from row r + 1
        # (or routes consisting only of starting at (m - 1, c))
        dp_from_below = [0] * n
        for c in range(n):
            if grid[m - 1][c] == '.':
                dp_from_below[c] = 1
                
        for r in range(m - 1, -1, -1):
            # 1. Compute dp_current_cell[c]: routes ending at (r, c) that are ready to move to row r - 1 (or finish if r == 0)
            dp_current_cell = [0] * n
            
            # Prefix sums of dp_from_below for fast range sum queries
            pref_from_below = [0] * (n + 1)
            for c in range(n):
                pref_from_below[c + 1] = (pref_from_below[c] + dp_from_below[c]) % MOD
                
            for c in range(n):
                if grid[r][c] == '.':
                    L = max(0, c - d)
                    R = min(n - 1, c + d)
                    # Sum of dp_from_below[k] for k != c such that |k - c| <= d
                    ways_from_other_cols = (pref_from_below[R + 1] - pref_from_below[L] - dp_from_below[c]) % MOD
                    dp_current_cell[c] = (dp_from_below[c] + ways_from_other_cols) % MOD
                    
            if r == 0:
                return sum(dp_current_cell) % MOD
                
            # 2. Compute dp_from_below for row r - 1: moving from row r to row r - 1
            next_dp_from_below = [0] * n
            
            if d >= 1:
                d_col_max = math.isqrt(d * d - 1)
                pref_current = [0] * (n + 1)
                for c in range(n):
                    pref_current[c + 1] = (pref_current[c] + dp_current_cell[c]) % MOD
                    
                for c_up in range(n):
                    if grid[r - 1][c_up] == '.':
                        L = max(0, c_up - d_col_max)
                        R = min(n - 1, c_up + d_col_max)
                        next_dp_from_below[c_up] = (pref_current[R + 1] - pref_current[L]) % MOD
                        
            dp_from_below = next_dp_from_below
            
        return 0
```
