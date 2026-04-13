class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        min_dist = len(nums)
        for i, num in enumerate(nums):
            if num == target:
                dist = abs(i - start)
                if dist < min_dist:
                    min_dist = dist
        return int(min_dist)
