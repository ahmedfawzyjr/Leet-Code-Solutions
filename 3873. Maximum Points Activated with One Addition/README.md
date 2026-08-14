# 3873. Maximum Points Activated with One Addition

**Difficulty**: Hard

## Problem Description

You are given a 2D integer array `points`, where `points[i] = [xi, yi]` represents the coordinates of the $i$-th point. All coordinates in `points` are **distinct**.

If a point is **activated**, then all points that have the **same** x-coordinate or y-coordinate become **activated** as well.

Activation continues until no additional points can be activated.

You may add **one additional** point at any integer coordinate `(x, y)` not already present in `points`. Activation begins by **activating this newly added point**.

Return an integer denoting the **maximum** number of points that can be activated, including the newly added point.

---

## Example 1

**Input**: `points = [[1,1],[1,2],[2,2]]`  
**Output**: `4`  
**Explanation**:
Adding and activating a point such as `(1, 3)` causes activations:
- `(1, 3)` shares $x = 1$ with `(1, 1)` and `(1, 2)` $\rightarrow$ `(1, 1)` and `(1, 2)` become activated.
- `(1, 2)` shares $y = 2$ with `(2, 2)` $\rightarrow$ `(2, 2)` becomes activated.

Thus, the activated points are `(1, 3)`, `(1, 1)`, `(1, 2)`, `(2, 2)`, so 4 points in total. We can show this is the maximum activated.

## Example 2

**Input**: `points = [[2,2],[1,1],[3,3]]`  
**Output**: `3`  
**Explanation**:
Adding and activating a point such as `(1, 2)` causes activations:
- `(1, 2)` shares $x = 1$ with `(1, 1)` $\rightarrow$ `(1, 1)` becomes activated.
- `(1, 2)` shares $y = 2$ with `(2, 2)` $\rightarrow$ `(2, 2)` becomes activated.

Thus, the activated points are `(1, 2)`, `(1, 1)`, `(2, 2)`, so 3 points in total. We can show this is the maximum activated.

## Example 3

**Input**: `points = [[2,3],[2,2],[1,1],[4,5]]`  
**Output**: `4`  
**Explanation**:
Adding and activating a point such as `(2, 1)` causes activations:
- `(2, 1)` shares $x = 2$ with `(2, 3)` and `(2, 2)` $\rightarrow$ `(2, 3)` and `(2, 2)` become activated.
- `(2, 1)` shares $y = 1$ with `(1, 1)` $\rightarrow$ `(1, 1)` becomes activated.

Thus, the activated points are `(2, 1)`, `(2, 3)`, `(2, 2)`, `(1, 1)`, so 4 points in total.

---

## Constraints

- $1 \le \text{points.length} \le 10^5$
- `points[i] = [xi, yi]`
- $-10^9 \le x_i, y_i \le 10^9$
- `points` contains all **distinct** coordinates.

---

## Solution Approach

### Bipartite Graph & Connected Components

1. **Graph Representation**:
   - Model each $x$-coordinate and $y$-coordinate as nodes in a graph.
   - Each given point $(x, y)$ acts as an edge connecting node `x` to node `y`.
   - Activation starting from any point in a connected component will activate **all** original points (edges) within that connected component.

2. **Connecting Components with 1 New Point**:
   - Placing a new point $(x_{\text{new}}, y_{\text{new}})$ connects node $x_{\text{new}}$ and node $y_{\text{new}}$.
   - If we pick $x_{\text{new}}$ from component $A$ and $y_{\text{new}}$ from component $B$ (where $A \neq B$), the new point merges component $A$ and component $B$.
   - The total number of activated original points will be $\text{size}(A) + \text{size}(B)$, plus $1$ for the newly added point itself.
   - If there is only $1$ component initially, adding a point connected to it (or anywhere) activates all points in that component $+ 1$.

3. **Algorithm**:
   - Use BFS / DFS / Disjoint Set Union (DSU) to find all connected components and count the number of points (edges) in each component.
   - Sort component sizes in descending order.
   - If there is $\ge 2$ components, the maximum activated points is $\text{size}_1 + \text{size}_2 + 1$.
   - If there is only $1$ component, the maximum activated points is $\text{size}_1 + 1$.

### Complexity Analysis
- **Time Complexity**: $O(N \log N)$ or $O(N)$ for building the graph, performing BFS/DFS component size counting, and sorting/finding the two largest component sizes.
- **Space Complexity**: $O(N)$ to store graph adjacency list / component mappings.

---

## Python Code

```python
from typing import List
from collections import defaultdict, deque

class Solution:
    def maxActivated(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for x, y in points:
            nx = ('x', x)
            ny = ('y', y)
            adj[nx].append(ny)
            adj[ny].append(nx)
            
        visited = set()
        comp_sizes = []
        
        for node in list(adj.keys()):
            if node not in visited:
                q = deque([node])
                visited.add(node)
                pts_count = 0
                while q:
                    curr = q.popleft()
                    if curr[0] == 'x':
                        pts_count += len(adj[curr])
                    for nxt in adj[curr]:
                        if nxt not in visited:
                            visited.add(nxt)
                            q.append(nxt)
                comp_sizes.append(pts_count)
                
        comp_sizes.sort(reverse=True)
        if len(comp_sizes) == 1:
            return comp_sizes[0] + 1
        else:
            return comp_sizes[0] + comp_sizes[1] + 1
```
