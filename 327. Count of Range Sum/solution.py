from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix_sums = [0]
        for x in nums:
            prefix_sums.append(prefix_sums[-1] + x)
        
        def count_while_merge_sort(sums, start, end):
            if end - start <= 1:
                return 0
            mid = (start + end) // 2
            count = count_while_merge_sort(sums, start, mid) + count_while_merge_sort(sums, mid, end)
            
            j = k = mid
            for i in range(start, mid):
                while j < end and sums[j] - sums[i] < lower:
                    j += 1
                while k < end and sums[k] - sums[i] <= upper:
                    k += 1
                count += k - j
            
            sums[start:end] = sorted(sums[start:end])
            return count
        
        return count_while_merge_sort(prefix_sums, 0, len(prefix_sums))
