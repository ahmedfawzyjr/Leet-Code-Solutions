# 1496. Path Crossing

Given a path made of `N`, `S`, `E`, and `W`, determine whether the path visits any location more than once.

## Examples

### Example 1

```text
Input: path = "NES"
Output: false
```

### Example 2

```text
Input: path = "NESWW"
Output: true
```

## Solution Approach

Track the current coordinate, starting at `(0, 0)`, and store every visited coordinate in a set. After each move, return `True` if the new coordinate is already in the set. Otherwise, add it and continue.

The starting coordinate is inserted before processing the path so returning to the origin is detected correctly.

## Complexity Analysis

- **Time Complexity:** `O(n)`, where `n` is the length of `path`.
- **Space Complexity:** `O(n)` for the visited-coordinate set.

## Python Code

```python
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        x = y = 0
        moves = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0),
        }

        for direction in path:
            dx, dy = moves[direction]
            x += dx
            y += dy
            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False
```
