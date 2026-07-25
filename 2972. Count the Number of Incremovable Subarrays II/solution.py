from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Find the maximum index l such that nums[0..l] is strictly increasing
        l = 0
        while l + 1 < n and nums[l] < nums[l + 1]:
            l += 1
            
        # If the entire array is strictly increasing, any non-empty subarray can be removed
        if l == n - 1:
            return n * (n + 1) // 2
            
        # Find the minimum index r such that nums[r..n-1] is strictly increasing
        r = n - 1
        while r - 1 >= 0 and nums[r - 1] < nums[r]:
            r -= 1
            
        # We can form valid remaining arrays by keeping a prefix nums[0..i-1] (i elements)
        # and a suffix nums[k..n-1] (n - k elements), where 0 <= i <= l + 1 and r <= k <= n.
        # We require k >= i + 1 (so the removed subarray nums[i..k-1] is non-empty)
        # and if i > 0 and k < n, nums[i - 1] < nums[k].
        
        ans = 0
        k = r
        for i in range(l + 2):
            target_k = max(r, i + 1)
            while k < n and (k < target_k or (i > 0 and nums[i - 1] >= nums[k])):
                k += 1
            ans += (n - k + 1)
            
        return ans
