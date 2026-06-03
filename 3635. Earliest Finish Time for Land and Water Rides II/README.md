# 3635. Earliest Finish Time for Land and Water Rides II

**Difficulty:** Medium

**Link:** [LeetCode](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/)

## Problem Description

You are given two categories of theme park attractions: **land rides** and **water rides**.

- **Land rides:**
    - `landStartTime[i]` - the earliest time the `i-th` land ride can be boarded.
    - `landDuration[i]` - how long the `i-th` land ride lasts.
- **Water rides:**
    - `waterStartTime[j]` - the earliest time the `j-th` water ride can be boarded.
    - `waterDuration[j]` - how long the `j-th` water ride lasts.

A tourist must experience **exactly one ride from each category**, in **either order**.

- A ride may be started at its opening time **or any later moment**.
- If a ride started at time `t`, it finishes at time `t + duration`.
- Immediately after finishing one ride, the tourist may board the other if it is already open, or wait until it opens.

Return the **earliest possible time** at which the tourist can finish both rides.

### Example 1:
**Input:** `landStartTime = [2,8]`, `landDuration = [4,1]`, `waterStartTime = [5]`, `waterDuration = [3]`  
**Output:** `9`  

### Example 2:
**Input:** `landStartTime = [5]`, `landDuration = [3]`, `waterStartTime = [1]`, `waterDuration = [10]`  
**Output:** `14`  

### Constraints:
- `1 <= n, m <= 10^5`
- `landStartTime.length == landDuration.length == n`
- `waterStartTime.length == waterDuration.length == m`
- `1 <= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] <= 10^9`

---

## Solution Analysis

The problem is similar to the first version but with significantly larger constraints ($N, M \le 10^5$), requiring an $O(N + M)$ solution instead of $O(N \times M)$.

### Optimized Greedy Approach

For a selected pair of rides $(i, j)$, there are two possible orders:

1.  **Case 1: Land ride $i$ then Water ride $j$**
    -   The land ride finishes at $T_{land\_finish} = landStartTime[i] + landDuration[i]$.
    -   The water ride can start at $\max(T_{land\_finish}, waterStartTime[j])$.
    -   The final finish time is $T_{final} = \max(T_{land\_finish}, waterStartTime[j]) + waterDuration[j]$.
    -   To minimize this for a fixed water ride $j$, we should choose land ride $i$ that minimizes $T_{land\_finish}$.
    -   Let $min\_land\_finish = \min_{i} (landStartTime[i] + landDuration[i])$.
    -   The best result for Case 1 is $\min_{j} (\max(min\_land\_finish, waterStartTime[j]) + waterDuration[j])$.

2.  **Case 2: Water ride $j$ then Land ride $i$**
    -   By symmetry, let $min\_water\_finish = \min_{j} (waterStartTime[j] + waterDuration[j])$.
    -   The best result for Case 2 is $\min_{i} (\max(min\_water\_finish, landStartTime[i]) + landDuration[i])$.

The overall minimum is the minimum of the results from Case 1 and Case 2.

**Complexity:**
- **Time Complexity:** $O(N + M)$ to find the minimum finish times and iterate through both lists once more.
- **Space Complexity:** $O(1)$ additional space beyond the input arrays.
