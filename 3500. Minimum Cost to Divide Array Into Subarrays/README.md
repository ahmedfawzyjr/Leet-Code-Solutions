# 3500. Minimum Cost to Divide Array Into Subarrays

**Difficulty**: Hard

## Problem Description
You are given two integer arrays, `nums` and `cost`, of the same size, and an integer `k`.

You can divide `nums` into contiguous subarrays. The cost of the $i$-th subarray consisting of elements `nums[l...r]` is:
$$\left( \text{sum}(\text{nums}[0...r]) + i \times k \right) \times \text{sum}(\text{cost}[l...r])$$

Note that $i$ represents the order of the subarray: $1$ for the first subarray, $2$ for the second, and so on.

Return the **minimum total cost** possible from any valid division of `nums` into subarrays.

---

## Example 1
**Input**: `nums = [3,1,4]`, `cost = [4,6,6]`, `k = 1`  
**Output**: `110`  
**Explanation**:
The minimum total cost can be achieved by dividing `nums` into subarrays `[3, 1]` and `[4]`.
- First subarray `[3, 1]`: $(3 + 1 + 1 \times 1) \times (4 + 6) = 50$.
- Second subarray `[4]`: $(3 + 1 + 4 + 2 \times 1) \times 6 = 60$.
Total cost = $50 + 60 = 110$.

## Example 2
**Input**: `nums = [4,8,5,1,14,2,2,12,1]`, `cost = [7,2,8,4,2,2,1,1,2]`, `k = 7`  
**Output**: `985`  

---

## Constraints
- `1 <= nums.length <= 1000`
- `cost.length == nums.length`
- `1 <= nums[i], cost[i] <= 1000`
- `1 <= k <= 1000`

---

## Solution Approach

### Dynamic Programming + Convex Hull Trick (CHT)

1. **Prefix Sums & DP Formulation**:
   Let $P[j] = \sum_{a=0}^{j-1} \text{nums}[a]$ and $C[j] = \sum_{a=0}^{j-1} \text{cost}[a]$.
   Let $dp[m][j]$ be the minimum cost to partition the prefix `nums[0...j-1]` into $m$ subarrays.
   
   The recurrence for the $m$-th subarray ending at index $j$ starting after $l$ (i.e. subarray `nums[l...j-1]`) is:
   $$dp[m][j] = \min_{m-1 \le l < j} \left\{ dp[m-1][l] + (P[j] + m \cdot k) \times (C[j] - C[l]) \right\}$$

2. **Convex Hull Optimization**:
   Rearranging the term inside the min:
   $$dp[m][j] = (P[j] + m \cdot k) \cdot C[j] + \min_{m-1 \le l < j} \left\{ -C[l] \cdot (P[j] + m \cdot k) + dp[m-1][l] \right\}$$
   
   For a fixed $m$, as $j$ increases:
   - Line slope: $m_{\text{line}} = -C[l]$ (strictly decreasing because $C[l]$ increases).
   - Line $y$-intercept: $c_{\text{line}} = dp[m-1][l]$.
   - Query point: $x = P[j] + m \cdot k$ (strictly increasing because $nums[j] > 0$).
   
   This directly matches the standard **Convex Hull Trick (CHT)** with monotonic slopes and queries!
   
3. **Complexity**:
   - **Time Complexity**: $O(N^2)$ — $N$ outer DP stages ($m = 1 \dots N$), each CHT line addition and query runs in amortized $O(1)$ time.
   - **Space Complexity**: $O(N)$ — space-optimized DP storing only the previous and current stage states.

---

## Python Code

```python
from typing import List

class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        n = len(nums)
        P = [0] * (n + 1)
        C = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + nums[i]
            C[i + 1] = C[i] + cost[i]

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        ans = float('inf')

        # CHT optimization for dp[m][j]
        for m in range(1, n + 1):
            next_dp = [float('inf')] * (n + 1)
            lines = []
            ptr = 0

            def add_line(m_line, c_line):
                line = (m_line, c_line)
                while len(lines) >= 2:
                    l1, l2 = lines[-2], lines[-1]
                    # Check if l2 is redundant
                    if (c_line - l1[1]) * (l1[0] - l2[0]) <= (l2[1] - l1[1]) * (l1[0] - m_line):
                        lines.pop()
                    else:
                        break
                lines.append(line)

            def query(x):
                nonlocal ptr
                if not lines:
                    return float('inf')
                if ptr >= len(lines):
                    ptr = len(lines) - 1
                while ptr + 1 < len(lines):
                    y1 = lines[ptr][0] * x + lines[ptr][1]
                    y2 = lines[ptr + 1][0] * x + lines[ptr + 1][1]
                    if y2 <= y1:
                        ptr += 1
                    else:
                        break
                return lines[ptr][0] * x + lines[ptr][1]

            for j in range(m, n + 1):
                l = j - 1
                if dp[l] != float('inf'):
                    add_line(-C[l], dp[l])
                x = P[j] + m * k
                val = query(x)
                if val != float('inf'):
                    next_dp[j] = val + x * C[j]
            
            dp = next_dp
            ans = min(ans, dp[n])

        return ans
```
