from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] | (1 << i))
        return res

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    n1 = 2
    print(f"Input: n = {n1}")
    print(f"Output: {sol.grayCode(n1)}")
    
    # Example 2
    n2 = 1
    print(f"Input: n = {n2}")
    print(f"Output: {sol.grayCode(n2)}")
