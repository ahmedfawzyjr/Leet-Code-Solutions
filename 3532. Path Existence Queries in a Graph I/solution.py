from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # Prefix sum of gaps where nums[i+1] - nums[i] > maxDiff
        # If pref[u] == pref[v], there are no gaps between u and v, hence they are in the same component.
        pref = [0] * n
        for i in range(1, n):
            pref[i] = pref[i-1]
            if nums[i] - nums[i-1] > maxDiff:
                pref[i] += 1
                
        ans = []
        for u, v in queries:
            ans.append(pref[u] == pref[v])
        return ans
