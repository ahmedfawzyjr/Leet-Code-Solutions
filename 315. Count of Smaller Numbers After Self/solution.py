from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        indices = list(range(n))
        
        def merge_sort(left, right):
            if right - left <= 1:
                return
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid, right)
            merge(left, mid, right)
            
        def merge(left, mid, right):
            i, j = left, mid
            temp = []
            right_count = 0
            while i < mid and j < right:
                if nums[indices[j]] < nums[indices[i]]:
                    temp.append(indices[j])
                    right_count += 1
                    j += 1
                else:
                    res[indices[i]] += right_count
                    temp.append(indices[i])
                    i += 1
            while i < mid:
                res[indices[i]] += right_count
                temp.append(indices[i])
                i += 1
            while j < right:
                temp.append(indices[j])
                j += 1
            indices[left:right] = temp
            
        merge_sort(0, n)
        return res
