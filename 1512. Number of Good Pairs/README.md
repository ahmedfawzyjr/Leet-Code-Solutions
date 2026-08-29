# 1512. Number of Good Pairs

**Difficulty:** Easy

## Problem Description

Given an array of integers `nums`, return the number of **good pairs**.

A pair `(i, j)` is called *good* if `nums[i] == nums[j]` and `i < j`.

### Example 1:

**Input:** `nums = [1,2,3,1,1,3]`  
**Output:** `4`  
**Explanation:** There are 4 good pairs `(0,3)`, `(0,4)`, `(3,4)`, `(2,5)` (0-indexed).
- Pair `(0, 3)`: `nums[0] == nums[3] == 1`
- Pair `(0, 4)`: `nums[0] == nums[4] == 1`
- Pair `(3, 4)`: `nums[3] == nums[4] == 1`
- Pair `(2, 5)`: `nums[2] == nums[5] == 3`

### Example 2:

**Input:** `nums = [1,1,1,1]`  
**Output:** `6`  
**Explanation:** Each pair in the array is good (combinations of 4 items taken 2 at a time: $\binom{4}{2} = 6$).

### Example 3:

**Input:** `nums = [1,2,3]`  
**Output:** `0`  
**Explanation:** No pairs satisfy `nums[i] == nums[j]`.

### Constraints:

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

---

## Solution Approach

### Single-Pass Hash Map (Running Count)

1. Maintain a hash map (`count` / `Counter`) to keep track of the frequency of each number seen so far.
2. As we iterate through `nums`:
   - Every prior appearance of the current value `nums[j]` can pair with index `j` to form a valid good pair `(i, j)` where $i < j$.
   - Add `count[nums[j]]` to our total count of good pairs.
   - Increment `count[nums[j]]` by `1`.
3. This achieves a clean, single-pass $O(N)$ solution without needing a secondary loop or explicit combination formula.

### Alternative Formula:

If we count all frequencies upfront, a number with count $k$ contributes $\frac{k(k - 1)}{2}$ good pairs. Summing this over all unique numbers yields the identical result.

---

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ where $N$ is the length of `nums`. We traverse the list once, performing $\mathcal{O}(1)$ average hash map lookups and updates per element.
- **Space Complexity:** $\mathcal{O}(U)$ where $U$ is the number of distinct elements in `nums` ($U \le \min(N, 100)$).

---

## Python Code

```python
from typing import List
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter()
        good_pairs = 0

        for num in nums:
            good_pairs += count[num]
            count[num] += 1

        return good_pairs
```
