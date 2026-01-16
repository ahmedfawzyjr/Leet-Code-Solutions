class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
        return res

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    n1 = 0b00000010100101000001111010011100
    res1 = sol.reverseBits(n1)
    print(f"Example 1 Output: {res1} ({bin(res1)})")
    # Expected: 964176192 (00111001011110000010100101000000)
    
    # Example 2
    n2 = 0b11111111111111111111111111111101
    res2 = sol.reverseBits(n2)
    print(f"Example 2 Output: {res2} ({bin(res2)})")
    # Expected: 3221225471 (10111111111111111111111111111111)
