from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        """
        Given a 0-indexed integer array nums, return an integer array answer of size n 
        where answer[i] = |leftSum[i] - rightSum[i]|.
        
        Complexity:
        - Time: O(N) where N is the length of nums.
        - Space: O(N) for the output array (or O(1) auxiliary space).
        """
        total_sum = sum(nums)
        left_sum = 0
        answer = []
        for num in nums:
            right_sum = total_sum - left_sum - num
            answer.append(abs(left_sum - right_sum))
            left_sum += num
        return answer
