from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] == n - mid:
                return n - mid
            elif citations[mid] < n - mid:
                left = mid + 1
            else:
                right = mid - 1
        return n - left

if __name__ == "__main__":
    s = Solution()
    test_cases = [
        ([0, 1, 3, 5, 6], 3),
        ([1, 2, 100], 2),
        ([0], 0),
        ([100], 1),
        ([0, 0, 0], 0)
    ]
    for citations, expected in test_cases:
        result = s.hIndex(citations)
        print(f"citations={citations}, expected={expected}, got={result}, {'PASS' if result == expected else 'FAIL'}")
