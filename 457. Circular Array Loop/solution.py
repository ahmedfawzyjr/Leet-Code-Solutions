from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        """
        Checks if there is a cycle in the circular array.
        Cycles must be unidirectional and length > 1.
        
        Time complexity: O(n)
        Space complexity: O(1)
        """
        n = len(nums)
        
        def get_next(i: int) -> int:
            return (i + nums[i]) % n
        
        for i in range(n):
            if nums[i] == 0:
                continue
            
            slow = i
            fast = get_next(i)
            
            # Check if unidirectional (all same sign)
            while nums[fast] * nums[i] > 0 and nums[get_next(fast)] * nums[i] > 0:
                if slow == fast:
                    # Check loop length > 1
                    if slow == get_next(slow):
                        break
                    return True
                
                slow = get_next(slow)
                fast = get_next(get_next(fast))
            
            # Mark visited as 0 to avoid re-processing
            curr = i
            while nums[curr] * nums[i] > 0:
                next_pos = get_next(curr)
                nums[curr] = 0
                curr = next_pos
                
        return False
