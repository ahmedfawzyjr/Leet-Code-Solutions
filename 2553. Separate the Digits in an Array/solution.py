from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        """
        Given an array of positive integers nums, return an array answer that consists 
        of the digits of each integer in nums after separating them in the same order 
        they appear in nums.
        
        Complexity:
        - Time: O(N * D), where N is the number of elements and D is the average number of digits.
        - Space: O(N * D) to store the result.
        """
        answer = []
        for num in nums:
            # Convert num to string to iterate through digits
            for digit in str(num):
                answer.append(int(digit))
        return answer
