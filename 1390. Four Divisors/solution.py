from typing import List
import math


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        """
        Return sum of divisors of integers that have exactly four divisors.
        
        For a number to have exactly 4 divisors, it must be either:
        1. p^3 (prime cubed): divisors are 1, p, p^2, p^3
        2. p * q (product of two distinct primes): divisors are 1, p, q, p*q
        
        Time Complexity: O(n * sqrt(max_num))
        Space Complexity: O(1)
        """
        total = 0
        
        for num in nums:
            divisors = self.get_divisors(num)
            if len(divisors) == 4:
                total += sum(divisors)
        
        return total
    
    def get_divisors(self, n: int) -> List[int]:
        """Get all divisors of n."""
        divisors = []
        
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
                
                # Early termination if more than 4 divisors
                if len(divisors) > 4:
                    return divisors
        
        return divisors
    
    def sumFourDivisors_optimized(self, nums: List[int]) -> int:
        """
        Optimized version: Count divisors and sum simultaneously.
        
        Time Complexity: O(n * sqrt(max_num))
        Space Complexity: O(1)
        """
        total = 0
        
        for num in nums:
            divisor_sum = 0
            divisor_count = 0
            
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisor_count += 1
                    divisor_sum += i
                    
                    if i != num // i:
                        divisor_count += 1
                        divisor_sum += num // i
                    
                    # Early termination
                    if divisor_count > 4:
                        break
            
            if divisor_count == 4:
                total += divisor_sum
        
        return total


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: nums = [21,4,7] -> Output: 32
    # 21 has divisors: 1, 3, 7, 21 (sum = 32)
    # 4 has divisors: 1, 2, 4 (only 3)
    # 7 has divisors: 1, 7 (only 2)
    print(sol.sumFourDivisors([21, 4, 7]))  # 32
    
    # Example 2: nums = [21,21] -> Output: 64
    print(sol.sumFourDivisors([21, 21]))  # 64
    
    # Example 3: nums = [1,2,3,4,5] -> Output: 0
    print(sol.sumFourDivisors([1, 2, 3, 4, 5]))  # 0
