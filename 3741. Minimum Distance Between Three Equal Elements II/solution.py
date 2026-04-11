from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        """
        Calculates the minimum distance of a good tuple (i, j, k) of distinct indices
        where nums[i] == nums[j] == nums[k].
        Distance = abs(i - j) + abs(j - k) + abs(k - i).
        For i < j < k, Distance = (j - i) + (k - j) + (k - i) = 2 * (k - i).
        """
        index_map = defaultdict(list)
        for i, num in enumerate(nums):
            index_map[num].append(i)
        
        min_dist = 10**18
        found = False
        
        for num in index_map:
            indices = index_map[num]
            if len(indices) >= 3:
                found = True
                # indices are naturally sorted as we appended them in order
                for i in range(len(indices) - 2):
                    # To minimize 2 * (indices[i+2] - indices[i]), we check triplets
                    dist = 2 * (indices[i+2] - indices[i])
                    if dist < min_dist:
                        min_dist = dist
        
        return min_dist if found else -1

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    print(f"Example 1: {sol.minimumDistance([1, 2, 1, 1, 3])}")  # Expected: 6
    # Example 2
    print(f"Example 2: {sol.minimumDistance([1, 1, 1, 1])}")     # Expected: 4
