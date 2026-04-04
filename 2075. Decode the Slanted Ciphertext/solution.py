class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        res = []
        
        # Matrix can be represented by encodedText[r * cols + c]
        # Diagonals start at (0, 0), (0, 1), (0, 2), ... (0, cols-1)
        for start_col in range(cols):
            for r in range(rows):
                c = start_col + r
                if c < cols:
                    res.append(encodedText[r * cols + c])
                else:
                    break
        
        # Join result and remove trailing spaces
        return "".join(res).rstrip()
