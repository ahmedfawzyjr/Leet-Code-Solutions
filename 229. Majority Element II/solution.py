from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # 1st pass: Find potential candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        # 2nd pass: Verify candidates
        result = []
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        n = len(nums)
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)
            
        return result

if __name__ == "__main__":
    sol = Solution()
    print(f"Majority [3,2,3]: {sol.majorityElement([3,2,3])}")
    print(f"Majority [1]: {sol.majorityElement([1])}")
    print(f"Majority [1,2]: {sol.majorityElement([1,2])}")
