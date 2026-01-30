class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        
        def countLessEqual(mid):
            count = 0
            c = n - 1
            for r in range(n):
                while c >= 0 and matrix[r][c] > mid:
                    c -= 1
                count += (c + 1)
            return count
        
        low = matrix[0][0]
        high = matrix[n-1][n-1]
        ans = low
        
        while low <= high:
            mid = (low + high) // 2
            if countLessEqual(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8)) # Expected: 13
    print(sol.kthSmallest([[-5]], 1)) # Expected: -5
