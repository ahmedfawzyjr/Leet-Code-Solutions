# 3568. Minimum Moves to Clean the Classroom

**Difficulty:** Medium  
**Topics:** Array, Breadth-First Search, Bit Manipulation, Matrix

## Problem Description

You are given an `m x n` grid `classroom` where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:

- `'S'`: Starting position of the student
- `'L'`: Litter that must be collected (once collected, the cell becomes empty)
- `'R'`: Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)
- `'X'`: Obstacle the student cannot pass through
- `'.'`: Empty space

You are also given an integer `energy`, representing the student's maximum energy capacity. The student starts with this energy from the starting position `'S'`.

Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area `'R'`, which resets the energy to its maximum capacity `energy`.

Return the **minimum** number of moves required to collect all litter items, or `-1` if it's impossible.

---

### Example 1:

**Input:** `classroom = ["S.", "XL"], energy = 2`  
**Output:** `2`  
**Explanation:**  
- The student starts at `(0, 0)` with energy `2`.
- Move 1: Move right to `(0, 1)`, energy becomes `1`.
- Move 2: Move down to `(1, 1)` and collect litter `L`, energy becomes `0`.
- All litter items have been collected in `2` moves.

### Example 2:

**Input:** `classroom = ["LS", "RL"], energy = 4`  
**Output:** `3`  
**Explanation:**  
- The student starts at `(0, 1)` with energy `4`.
- Move 1: Move left to `(0, 0)` to collect litter `L`, energy becomes `3`.
- Move 2: Move down to `(1, 0)` on reset area `R`, restoring energy to `4`.
- Move 3: Move right to `(1, 1)` to collect litter `L`, energy becomes `3`.
- All litter items collected in `3` moves.

### Example 3:

**Input:** `classroom = ["L.S", "RXL"], energy = 2`  
**Output:** `-1`  
**Explanation:**  
- The student cannot collect all litter items without running out of energy before reaching a reset area or all litter.

---

### Constraints:

- $1 \le m, n \le 20$
- $1 \le \text{energy} \le 50$
- `classroom[i][j]` is one of `'S'`, `'L'`, `'R'`, `'X'`, or `'.'`.
- There is exactly one `'S'` in the grid.
- There are at most $10$ `'L'` cells in the grid.

---

## Solution Approach

### Bitmask BFS with State Pruning

1. **Bitmask State Representation:**
   - We assign each of the $K$ litter items a unique index from $0$ to $K - 1$.
   - A bitmask of length $K$ (ranging from $0$ to $2^K - 1$) tracks the subset of collected litter items.
   - When all litters are collected, $\text{mask} = 2^K - 1$.

2. **Breadth-First Search (BFS):**
   - Since every movement step has a uniform cost of $1$ move, BFS explores paths in strictly non-decreasing order of moves, guaranteeing that the first time all litters are collected, the move count is minimal.
   - State in queue: `(r, c, mask, cur_energy, moves)`.

3. **Pruning with Maximum Remaining Energy:**
   - Maintain a 3D table `max_e[r][c][mask]` initialized to `-1`.
   - If we reach cell `(r, c)` with collection status `mask` and remaining energy `ne <= max_e[r][c][mask]`, this state is strictly dominated (same or greater moves, with less or equal energy) and can be pruned.
   - If `ne > max_e[r][c][mask]`, we update `max_e[r][c][mask] = ne` and enqueue the new state.

4. **Energy Transition Rules:**
   - Moving costs 1 unit: `ne = e - 1`.
   - If landing on `'R'`: energy restores to full capacity (`ne = energy`).
   - If landing on `'L'`: set the corresponding bit in `mask`. If $\text{nmask} = 2^K - 1$, we return $\text{moves} + 1$ immediately.
   - If `ne == 0` and the cell is not `'R'`, it is a dead end (no future moves can be made from this cell).

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(m \cdot n \cdot 2^K)$, where $m, n \le 20$ and $K \le 10$ is the number of litter items.
  - The total number of `(r, c, mask)` states is $m \cdot n \cdot 2^K \le 20 \times 20 \times 1024 = 409,600$.
  - With the energy dominance pruning, each `(r, c, mask)` is enqueued only when a strictly higher energy level is found.
- **Space Complexity:** $\mathcal{O}(m \cdot n \cdot 2^K)$ auxiliary space for the `max_e` memoization table and the BFS queue.
