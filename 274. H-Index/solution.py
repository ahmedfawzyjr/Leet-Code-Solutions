from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1
            else:
                break
        return h

if __name__ == "__main__":
    s = Solution()
    test_cases = [
        ([3, 0, 6, 1, 5], 3),
        ([1, 3, 1], 1),
        ([100], 1),
        ([0], 0)
    ]
    for citations, expected in test_cases:
        # Create a copy as sort modifies in-place
        result = s.hIndex(citations[:])
        print(f"citations={citations}, expected={expected}, got={result}, {'PASS' if result == expected else 'FAIL'}")
