# 61. Rotate List

**Difficulty:** Medium

## Problem Description

Given the `head` of a linked list, rotate the list to the right by `k` places.

### Example 1:
![Example 1](https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg)
- **Input:** `head = [1,2,3,4,5], k = 2`
- **Output:** `[4,5,1,2,3]`

### Example 2:
![Example 2](https://assets.leetcode.com/uploads/2020/11/13/rotate2.jpg)
- **Input:** `head = [0,1,2], k = 4`
- **Output:** `[2,0,1]`

### Constraints:
- The number of nodes in the list is in the range `[0, 500]`.
- `-100 <= Node.val <= 100`
- `0 <= k <= 2 * 10^9`

## Solution Approach

1.  **Find the length**: Traverse the list to find its length and the tail node.
2.  **Handle k**: Since `k` can be very large, take `k = k % length`. If `k` is 0, no rotation is needed.
3.  **Find the split point**: The new tail will be at position `length - k - 1` (0-indexed).
4.  **Rotate**:
    - Connect the old tail to the old head to form a cycle.
    - Move to the new tail.
    - Set the new head as `new_tail.next`.
    - Break the cycle by setting `new_tail.next = None`.

## Complexity Analysis

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the linked list. We traverse the list once to find the length and once more to find the split point.
- **Space Complexity:** $O(1)$, as we only use a few pointers.
