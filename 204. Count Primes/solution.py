class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        primes = [True] * n
        primes[0] = primes[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
                    
        return sum(primes)

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    n = 10
    print(f"Example 1: {sol.countPrimes(n)}") # Expected: 4
    
    # Example 2
    n = 0
    print(f"Example 2: {sol.countPrimes(n)}") # Expected: 0
    
    # Example 3
    n = 1
    print(f"Example 3: {sol.countPrimes(n)}") # Expected: 0
