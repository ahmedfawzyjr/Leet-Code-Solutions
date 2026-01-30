class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        if n < 2:
            return n
        
        # Greedy approach
        # Count the number of peaks and valleys
        
        count = 1
        prev_diff = 0
        
        for i in range(1, n):
            diff = nums[i] - nums[i-1]
            if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
                count += 1
                prev_diff = diff
        
        return count

if __name__ == "__main__":
    sol = Solution()
    print(sol.wiggleMaxLength([1,7,4,9,2,5])) # Expected: 6
    print(sol.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])) # Expected: 7
    print(sol.wiggleMaxLength([1,2,3,4,5,6,7,8,9])) # Expected: 2
