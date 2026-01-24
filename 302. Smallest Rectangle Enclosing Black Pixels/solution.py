from typing import List

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        rows = len(image)
        cols = len(image[0])
        
        def search(start, end, check, first):
            while start < end:
                mid = (start + end) // 2
                if check(mid) == first:
                    end = mid
                else:
                    start = mid + 1
            return start
            
        def check_row(r):
            return '1' in image[r]
            
        def check_col(c):
            return any(image[r][c] == '1' for r in range(rows))
            
        top = search(0, x, check_row, True)
        bottom = search(x + 1, rows, check_row, False)
        left = search(0, y, check_col, True)
        right = search(y + 1, cols, check_col, False)
        
        return (bottom - top) * (right - left)
