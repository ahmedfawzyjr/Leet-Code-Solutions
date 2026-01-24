class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def getMax(nums, k):
            stack = []
            to_remove = len(nums) - k
            for num in nums:
                while stack and stack[-1] < num and to_remove > 0:
                    stack.pop()
                    to_remove -= 1
                stack.append(num)
            return stack[:k]

        def merge(nums1, nums2):
            res = []
            while nums1 or nums2:
                if nums1 > nums2:
                    res.append(nums1.pop(0))
                else:
                    res.append(nums2.pop(0))
            return res

        max_res = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            res = merge(getMax(nums1, i), getMax(nums2, k - i))
            if res > max_res:
                max_res = res
        return max_res
