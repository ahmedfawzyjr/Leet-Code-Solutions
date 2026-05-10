class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # dp[i] stores the maximum number of jumps to reach index i from index 0.
        # Initialize with -1 to indicate that the index is not reachable yet.
        dp = [-1] * n
        dp[0] = 0
        
        for i in range(n):
            # If the current index i is not reachable from 0, skip it.
            if dp[i] == -1:
                continue
            
            for j in range(i + 1, n):
                # Check the jumping condition: -target <= nums[j] - nums[i] <= target
                if abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        return dp[n - 1]
