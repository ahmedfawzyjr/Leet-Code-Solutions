class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_nodes(prefix, n):
            curr = prefix
            next_prefix = prefix + 1
            count = 0
            while curr <= n:
                count += min(n + 1, next_prefix) - curr
                curr *= 10
                next_prefix *= 10
            return count
        
        curr = 1
        k -= 1
        while k > 0:
            count = count_nodes(curr, n)
            if count <= k:
                k -= count
                curr += 1
            else:
                k -= 1
                curr *= 10
        return curr
