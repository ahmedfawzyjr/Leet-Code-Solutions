# 3953. Maximum Score with Co-Prime Element

**Difficulty**: Hard

## Problem Description

You are given an integer array `nums` of length `n` and an integer `maxVal`.

You **may** change any element in `nums` to any positive integer **less than or equal** to `maxVal`. Each such change costs `1`.

Two integers are **co-prime** if their **greatest common divisor (GCD)** is `1`.

After all modifications, you **must** choose an index `i` such that `nums[i]` is **co-prime** with every other element `nums[j]` ($j \neq i$).

Let:
- `selectedValue` be the final value of `nums[i]` after modifications.
- `modificationCost` be the total number of elements changed.

The score is defined as $\text{score} = \text{selectedValue} - \text{modificationCost}$.

Return the **maximum** possible score.

---

## Example 1

**Input**: `nums = [3,4,6], maxVal = 5`  
**Output**: `4`  
**Explanation**:  
Change `nums[2]` from `6` to `5`, which costs 1. Choose `nums[2] = 5`, since it is co-prime with 3 and 4.
- `selectedValue = 5`
- `modificationCost = 1`
- The score is $5 - 1 = 4$.

## Example 2

**Input**: `nums = [1,2,3], maxVal = 4`  
**Output**: `3`  
**Explanation**:  
No modifications are required. Choose `nums[2] = 3`, since it is co-prime with 1 and 2.
- `selectedValue = 3`
- `modificationCost = 0`
- The score is $3 - 0 = 3$.

## Example 3

**Input**: `nums = [2,2], maxVal = 1`  
**Output**: `1`  
**Explanation**:  
Change `nums[0]` from 2 to 1, which costs 1. Choose `nums[1] = 2`, since it is co-prime with 1.
- `selectedValue = 2`
- `modificationCost = 1`
- The score is $2 - 1 = 1$.

---

## Constraints

- $1 \le \text{nums.length} \le 10^5$
- $1 \le \text{nums}[i] \le 10^5$
- $1 \le \text{maxVal} \le 10^5$

---

## Solution Approach

### Principle of Inclusion-Exclusion (PIE) & Sieve

1. **Analysis of Modifications**:
   - Suppose we fix the chosen element index $i$ to have final value $v$.
   - Any other element $j \neq i$ with $\gcd(\text{nums}[j], v) > 1$ must be modified to be coprime to $v$. Since we can always modify it to `1` (which is coprime to all integers and $\le \text{maxVal}$ since $\text{maxVal} \ge 1$), each such conflicting element contributes exactly $1$ to the modification cost.
   - Elements with $\gcd(\text{nums}[j], v) = 1$ do not need to be changed.

2. **Counting Conflicting Elements**:
   - Two numbers share a common factor $> 1$ if and only if they share at least one prime factor.
   - For a candidate value $v$, let $C(v)$ denote the total count of elements in the original `nums` that share at least one prime factor with $v$.
   - Since any number $\le 10^5$ has at most 6 distinct prime factors, we can compute $C(v)$ using the **Principle of Inclusion-Exclusion (PIE)** over the subsets of prime factors of $v$:
     $$C(v) = \sum_{\emptyset \neq S \subseteq \text{primes}(v)} (-1)^{|S| + 1} \cdot \text{cnt}[\prod_{p \in S} p]$$
     where $\text{cnt}[d]$ is the number of elements in `nums` divisible by $d$.

3. **Evaluating Candidate Values**:
   - **Option A (Keep an existing element unchanged)**:
     - For any distinct value $v$ present in `nums`, we can pick an index $i$ where $\text{nums}[i] = v$ and leave it unchanged.
     - The cost to fix all other conflicting elements is $C(v) - 1$.
     - $\text{Score} = v - (C(v) - 1)$.
   - **Option B (Modify an element to $v \in [1, \text{maxVal}]$)**:
     - If $C(v) > 0$, we can choose to change one of the conflicting elements $i$ to $v$. The cost for $i$ is $1$, and the remaining $C(v) - 1$ conflicting elements cost $C(v) - 1$. Total cost = $C(v)$.
     - If $C(v) = 0$, all elements are already coprime to $v$. Changing any element to $v$ costs $1$.
     - $\text{Score} = v - \text{cost}$.

4. **Time Complexity**:
   - Sieve & prime factorization: $O(M \log \log M)$.
   - Counting multiples for all divisors: $O(M \log M)$ where $M = \max(\max(\text{nums}), \text{maxVal})$.
   - PIE queries for all $v \le M$: $\sum 2^{\omega(v)} = O(M)$.
   - Total Time Complexity: $O(N + M \log M) \approx O(N + M \log M)$, which comfortably runs within time limits.
   - Space Complexity: $O(M)$ for the sieve and divisor counts.

---

## Python Code

```python
from typing import List

class Solution:
    def maxScore(self, nums: List[int], maxVal: int) -> int:
        n = len(nums)
        if n == 1:
            return max(nums[0], maxVal - (1 if nums[0] != maxVal else 0))

        MAX_V = max(max(nums), maxVal)

        # Precompute smallest prime factor (SPF)
        spf = list(range(MAX_V + 1))
        for i in range(2, int(MAX_V**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, MAX_V + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # Precompute distinct prime factors for each number
        prime_factors = [[] for _ in range(MAX_V + 1)]
        for i in range(2, MAX_V + 1):
            temp = i
            factors = []
            while temp > 1:
                p = spf[temp]
                factors.append(p)
                while temp % p == 0:
                    temp //= p
            prime_factors[i] = factors

        # Count frequencies of each number in nums
        freq = [0] * (MAX_V + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = count of numbers in nums divisible by d
        cnt = [0] * (MAX_V + 1)
        for d in range(1, MAX_V + 1):
            for multiple in range(d, MAX_V + 1, d):
                cnt[d] += freq[multiple]

        # Function to count elements in nums sharing a prime factor with v (using PIE)
        def count_conflicts(v: int) -> int:
            if v == 1:
                return 0
            primes = prime_factors[v]
            k = len(primes)
            res = 0
            for mask in range(1, 1 << k):
                prod = 1
                bits = 0
                for j in range(k):
                    if (mask >> j) & 1:
                        prod *= primes[j]
                        bits += 1
                if bits % 2 == 1:
                    res += cnt[prod]
                else:
                    res -= cnt[prod]
            return res

        ans = -float('inf')

        # Option 1: Pick an index i and KEEP nums[i] (v = nums[i])
        for v in range(1, MAX_V + 1):
            if freq[v] > 0:
                conflicts = count_conflicts(v)
                # Other conflicting elements count is conflicts - 1
                cost = conflicts - 1
                ans = max(ans, v - cost)

        # Option 2: Pick an index i and CHANGE nums[i] to v in [1, maxVal]
        for v in range(1, maxVal + 1):
            conflicts = count_conflicts(v)
            if conflicts > 0:
                cost = conflicts
            else:
                cost = 1
            ans = max(ans, v - cost)

        return ans
```
