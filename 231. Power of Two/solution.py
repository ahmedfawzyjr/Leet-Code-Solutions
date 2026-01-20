class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

if __name__ == "__main__":
    sol = Solution()
    print(f"Is 1 power of two? {sol.isPowerOfTwo(1)}") # True
    print(f"Is 16 power of two? {sol.isPowerOfTwo(16)}") # True
    print(f"Is 3 power of two? {sol.isPowerOfTwo(3)}") # False
