from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        common = 0
        C = []
        for a, b in zip(A, B):
            if a in seen:
                common += 1
            else:
                seen.add(a)
            if b in seen:
                common += 1
            else:
                seen.add(b)
            C.append(common)
        return C

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    A1 = [1, 3, 2, 4]
    B1 = [3, 1, 2, 4]
    print(f"Input: A = {A1}, B = {B1}")
    print(f"Output: {solution.findThePrefixCommonArray(A1, B1)}")
    # Expected: [0, 2, 3, 4]
    
    # Example 2
    A2 = [2, 3, 1]
    B2 = [3, 1, 2]
    print(f"Input: A = {A2}, B = {B2}")
    print(f"Output: {solution.findThePrefixCommonArray(A2, B2)}")
    # Expected: [0, 1, 3]
