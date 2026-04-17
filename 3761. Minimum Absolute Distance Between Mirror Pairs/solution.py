from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def get_reverse(n: int) -> int:
            return int(str(n)[::-1])
        
        # last_seen_rev[r] stores the largest index i such that reverse(nums[i]) == r
        last_seen_rev = {} 
        min_dist = float('inf')
        
        for j, val in enumerate(nums):
            # Check if this val matches any previous reverse(nums[i])
            if val in last_seen_rev:
                min_dist = min(min_dist, j - last_seen_rev[val])
            
            # Store the reverse of current nums[j] to match later nums[k]
            rev_val = get_reverse(val)
            # Update to the latest index to minimize distance for future matches
            last_seen_rev[rev_val] = j
            
        return int(min_dist) if min_dist != float('inf') else -1

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    print(sol.minMirrorPairDistance([12, 21, 45, 33, 54])) # Expected: 1
    # Example 2 (based on trace logic)
    print(sol.minMirrorPairDistance([1, 10, 100])) # Expected: -1 (reverse(1)=1, reverse(10)=1, reverse(100)=1. None match nums[j])
    # Let's try [10, 1]
    print(sol.minMirrorPairDistance([10, 1])) # Expected: 1
