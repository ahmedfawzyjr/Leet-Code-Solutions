from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
        return []

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    numbers1 = [2,7,11,15]
    target1 = 9
    print(f"Example 1 Output: {sol.twoSum(numbers1, target1)}") # Expected: [1, 2]
    
    # Example 2
    numbers2 = [2,3,4]
    target2 = 6
    print(f"Example 2 Output: {sol.twoSum(numbers2, target2)}") # Expected: [1, 3]
    
    # Example 3
    numbers3 = [-1,0]
    target3 = -1
    print(f"Example 3 Output: {sol.twoSum(numbers3, target3)}") # Expected: [1, 2]
