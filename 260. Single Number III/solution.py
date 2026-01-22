from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        
        # Find the rightmost set bit
        # xor_sum & -xor_sum extracts the lowest set bit
        diff = xor_sum & -xor_sum
        
        a, b = 0, 0
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num
                
        return [a, b]

if __name__ == "__main__":
    s = Solution()
    test_cases = [
        ([1, 2, 1, 3, 2, 5], {3, 5}),
        ([-1, 0], {-1, 0}),
        ([0, 1], {1, 0})
    ]
    for nums, expected_set in test_cases:
        result = s.singleNumber(nums)
        result_set = set(result)
        print(f"nums={nums}, expected={expected_set}, got={result}, {'PASS' if result_set == expected_set else 'FAIL'}")
