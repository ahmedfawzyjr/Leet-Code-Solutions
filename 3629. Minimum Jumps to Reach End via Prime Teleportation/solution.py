import collections

class Solution:
    def minJumps(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        max_val = max(nums)
        # Sieve for primes up to max_val
        is_prime = [True] * (max_val + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(max_val**0.5) + 1):
            if is_prime[p]:
                for i in range(p * p, max_val + 1, p):
                    is_prime[i] = False
        
        # Precompute smallest prime factor for factorization
        spf = list(range(max_val + 1))
        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:
                for j in range(i*i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i
        
        # prime_to_multiples_indices[p] will store all indices j such that nums[j] % p == 0
        prime_to_multiples_indices = collections.defaultdict(list)
        
        def get_distinct_prime_factors(x):
            factors = set()
            while x > 1:
                factors.add(spf[x])
                x //= spf[x]
            return factors

        for i, num in enumerate(nums):
            factors = get_distinct_prime_factors(num)
            for p in factors:
                prime_to_multiples_indices[p].append(i)
        
        # BFS
        queue = collections.deque([(0, 0)])
        visited = [False] * n
        visited[0] = True
        prime_used = [False] * (max_val + 1)
        
        while queue:
            curr_idx, dist = queue.popleft()
            
            if curr_idx == n - 1:
                return dist
            
            # Adjacent steps
            for next_idx in [curr_idx - 1, curr_idx + 1]:
                if 0 <= next_idx < n and not visited[next_idx]:
                    visited[next_idx] = True
                    queue.append((next_idx, dist + 1))
            
            # Prime teleportation
            val = nums[curr_idx]
            if val <= max_val and is_prime[val] and not prime_used[val]:
                prime_used[val] = True
                for next_idx in prime_to_multiples_indices[val]:
                    if not visited[next_idx]:
                        visited[next_idx] = True
                        queue.append((next_idx, dist + 1))
                        
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.minJumps([1, 2, 4, 6]))  # Output: 2
    print(sol.minJumps([2, 3, 4, 7, 9]))  # Output: 2
    print(sol.minJumps([4, 6, 5, 8]))  # Output: 3
