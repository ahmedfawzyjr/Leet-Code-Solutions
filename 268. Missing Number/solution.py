from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

if __name__ == "__main__":
    s = Solution()
    test_cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8)
    ]
    for nums, expected in test_cases:
        result = s.missingNumber(nums)
        print(f"nums={nums}, expected={expected}, got={result}, {'PASS' if result == expected else 'FAIL'}")
