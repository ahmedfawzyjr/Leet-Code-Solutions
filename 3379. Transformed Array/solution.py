from typing import List

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        """
        Constructs a transformed array based on circular movement rules.
        
        Time complexity: O(n)
        Space complexity: O(n) for the result array.
        """
        n = len(nums)
        result = [0] * n
        for i in range(n):
            if nums[i] == 0:
                result[i] = nums[i]
            else:
                # Calculate the target index using modulo arithmetic for circular wrap-around
                target_index = (i + nums[i]) % n
                result[i] = nums[target_index]
        return result
