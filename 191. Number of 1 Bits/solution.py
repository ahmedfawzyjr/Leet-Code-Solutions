class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    n1 = 11
    print(f"Example 1 Output: {sol.hammingWeight(n1)}")
    # Expected: 3
    
    # Example 2
    n2 = 128
    print(f"Example 2 Output: {sol.hammingWeight(n2)}")
    # Expected: 1
    
    # Example 3
    n3 = 2147483645
    print(f"Example 3 Output: {sol.hammingWeight(n3)}")
    # Expected: 30
