class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Step 1: Precompute prime scores using Sieve of Eratosthenes
        max_val = max(nums)
        prime_scores = [0] * (max_val + 1)
        for i in range(2, max_val + 1):
            if prime_scores[i] == 0:  # i is prime
                for j in range(i, max_val + 1, i):
                    prime_scores[j] += 1

        scores = [prime_scores[x] for x in nums]

        # Step 2: Monotonic stack to find left and right bounds for each element
        # left[i]: nearest index to left with prime_score >= prime_score[i]
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and scores[stack[-1]] < scores[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        # right[i]: nearest index to right with prime_score > prime_score[i]
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and scores[stack[-1]] <= scores[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        # Step 3: Calculate contribution (number of subarrays) for each index
        # Sort elements by value in descending order to greedily pick largest multipliers
        elements = []
        for i in range(n):
            count = (i - left[i]) * (right[i] - i)
            elements.append((nums[i], count))

        elements.sort(key=lambda x: x[0], reverse=True)

        # Step 4: Greedily multiply the largest elements
        ans = 1
        for val, count in elements:
            take = min(k, count)
            ans = (ans * pow(val, take, MOD)) % MOD
            k -= take
            if k == 0:
                break

        return ans
