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
