class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        # dp[i] is the number of ways to reach sum i
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        
        return dp[target]

if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum4([1,2,3], 4)) # Expected: 7
    print(sol.combinationSum4([9], 3)) # Expected: 0
