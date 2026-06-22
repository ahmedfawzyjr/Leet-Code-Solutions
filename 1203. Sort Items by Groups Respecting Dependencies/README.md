# 1203. Sort Items by Groups Respecting Dependencies

**Difficulty:** Hard

**Link:** [LeetCode](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/)

## Problem Description

There are `n` items, each belonging to either one group or no group at all. For each item `i`, `group[i]` is the group index, or `-1` if the item has no group.

We are also given a dependency list `beforeItems[i]`, where every item in `beforeItems[i]` must appear before item `i` in the final ordering.

Return any valid order of the items such that:
- all items in the same group appear consecutively, and
- all dependencies are respected.

If no valid order exists, return `[]`.

### Example 1
**Input:**
- `n = 8`
- `m = 2`
- `group = [-1, -1, 1, 0, 0, 1, 0, -1]`
- `beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]`

**Output:**
- `[6, 3, 4, 1, 5, 2, 0, 7]`

### Example 2
**Input:**
- Same as Example 1, except `beforeItems[6] = [4]`

**Output:**
- `[]`

---

## Solution Analysis

This problem is a combination of two topological sort problems:

1. **Within each group**: items in the same group must be ordered so that their internal dependencies are respected.
2. **Across groups**: if one group depends on another, the groups themselves must also be topologically ordered.

### Approach
- Build a dependency graph on items.
- For each group, run a topological sort on the items inside that group only.
- Build another graph on groups, where an edge `A -> B` means some item in group `A` must come before some item in group `B`.
- Run topological sort on the groups.
- Concatenate the items of groups in the resulting group order.

If either topological sort fails, the answer is `[]`.

### Complexity
- **Time Complexity:** `O(n + e)` where `e` is the number of dependency edges.
- **Space Complexity:** `O(n + e)`.

---

## Code

Refer to [solution.py](./solution.py) for the complete implementation.
