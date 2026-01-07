class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        Dutch National Flag algorithm - One pass O(n) solution.
        Uses three pointers to partition the array into three sections:
        - [0, low): all 0s
        - [low, mid): all 1s
        - [high, n): all 2s
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap with low pointer and move both forward
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 is in correct position, just move mid forward
                mid += 1
            else:  # nums[mid] == 2
                # Swap with high pointer and move high backward
                # Don't move mid because swapped element needs to be checked
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    nums1 = [2, 0, 2, 1, 1, 0]
    sol.sortColors(nums1)
    print(f"Test 1: {nums1}")  # Expected: [0, 0, 1, 1, 2, 2]
    
    # Test case 2
    nums2 = [2, 0, 1]
    sol.sortColors(nums2)
    print(f"Test 2: {nums2}")  # Expected: [0, 1, 2]
