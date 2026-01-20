from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        ranges = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            # If current number is not consecutive to the previous one
            if nums[i] != nums[i-1] + 1:
                if start == nums[i-1]:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{nums[i-1]}")
                start = nums[i]
        
        # Handle the last range
        if start == nums[-1]:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{nums[-1]}")
            
        return ranges

if __name__ == "__main__":
    sol = Solution()
    print(f"Ranges [0,1,2,4,5,7]: {sol.summaryRanges([0,1,2,4,5,7])}")
    print(f"Ranges [0,2,3,4,6,8,9]: {sol.summaryRanges([0,2,3,4,6,8,9])}")
