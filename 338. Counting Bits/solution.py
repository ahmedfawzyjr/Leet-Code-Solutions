from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            # ans[i] = ans[i // 2] + (i % 2)
            ans[i] = ans[i >> 1] + (i & 1)
        return ans

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    n1 = 2
    print(f"Example 1: {sol.countBits(n1)}") # Expected: [0, 1, 1]
    
    # Example 2
    n2 = 5
    print(f"Example 2: {sol.countBits(n2)}") # Expected: [0, 1, 1, 2, 1, 2]
