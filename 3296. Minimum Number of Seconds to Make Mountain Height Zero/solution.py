import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        def can_reduce(T):
            total_reduced = 0
            for w in workerTimes:
                # A worker with workerTime 'w' can reduce the height by 'x' units in time 'T' if:
                # w * (x * (x + 1) / 2) <= T
                # x^2 + x - 2T/w <= 0
                # Solving for x: x = (-1 + sqrt(1 + 8T/w)) / 2
                x = int((-1 + math.sqrt(1 + 8 * T / w)) / 2)
                total_reduced += x
                if total_reduced >= mountainHeight:
                    return True
            return total_reduced >= mountainHeight

        low = 0
        # Upper bound calculation:
        # If there's only one worker with the maximum possible workerTime (10^6)
        # and the mountain height is at its maximum (10^5):
        # T = 10^6 * (10^5 * (10^5 + 1) / 2) ≈ 5 * 10^15
        high = 10**16 
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_reduce(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
