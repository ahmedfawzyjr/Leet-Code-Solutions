# 3633. Earliest Finish Time for Land and Water Rides I

**Difficulty:** Easy

**Link:** [LeetCode](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/)

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
**Explanation:**  
- Plan A (land ride 0 -> water ride 0):  
  Start land ride 0 at time 2. Finish at 2 + 4 = 6.  
  Water ride 0 opens at 5. Start at 6. Finish at 6 + 3 = 9.
- Plan B (water ride 0 -> land ride 0):  
  Start water ride 0 at time 5. Finish at 5 + 3 = 8.  
  Land ride 0 opens at 2. Start at 8. Finish at 8 + 4 = 12.
- Plan C (land ride 1 -> water ride 0):  
  Start land ride 1 at time 8. Finish at 8 + 1 = 9.  
  Water ride 0 opens at 5. Start at 9. Finish at 9 + 3 = 12.
- Plan D (water ride 0 -> land ride 1):  
  Start water ride 0 at time 5. Finish at 5 + 3 = 8.  
  Land ride 1 opens at 8. Start at 8. Finish at 8 + 1 = 9.
Plan A and D give the correct finish time of 9.

### Example 2:
**Input:** `landStartTime = [5]`, `landDuration = [3]`, `waterStartTime = [1]`, `waterDuration = [10]`  
**Output:** `14`  
**Explanation:**  
- Plan A (water ride 0 -> land ride 0):  
  Start water ride 0 at time 1. Finish at 11.  
  Land ride 0 opens at 5. Start immediately at 11 and finish at 11 + 3 = 14.
- Plan B (land ride 0 -> water ride 0):  
  Start land ride 0 at time 5. Finish at 8.  
  Water ride 0 opens at 1. Start immediately at 8 and finish at 8 + 10 = 18.
Plan A provides the earliest finish time of 14.

### Constraints:
- `1 <= n, m <= 100`
- `landStartTime.length == landDuration.length == n`
- `waterStartTime.length == waterDuration.length == m`
- `1 <= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] <= 1000`

---

## Solution Analysis

Since we only need to pick one ride from each category and the number of rides is small ($N, M \le 100$), we can iterate through all possible pairs of (land ride, water ride) and check both possible orders (Land then Water, or Water then Land).

### Brute Force Approach

1.  Iterate through each land ride $i \in [0, n-1]$.
2.  Iterate through each water ride $j \in [0, m-1]$.
3.  Calculate the finish time for two cases:
    -   **Case 1: Land then Water**
        -   $T_{land\_finish} = landStartTime[i] + landDuration[i]$
        -   $T_{water\_start} = \max(T_{land\_finish}, waterStartTime[j])$
        -   $T_{final1} = T_{water\_start} + waterDuration[j]$
    -   **Case 2: Water then Land**
        -   $T_{water\_finish} = waterStartTime[j] + waterDuration[j]$
        -   $T_{land\_start} = \max(T_{water\_finish}, landStartTime[i])$
        -   $T_{final2} = T_{land\_start} + landDuration[i]$
4.  Keep track of the minimum $T_{final}$ across all pairs and orders.

**Complexity:**
- **Time Complexity:** $O(N \times M)$, where $N$ and $M$ are the number of land and water rides respectively.
- **Space Complexity:** $O(1)$.
