from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        
        for word in words:
            if length + len(line) + len(word) > maxWidth:
                # Line is full
                for i in range(maxWidth - length):
                    line[i % (len(line) - 1 or 1)] += ' '
                res.append("".join(line))
                line, length = [], 0
            
            line.append(word)
            length += len(word)
            
        # Last line
        res.append(" ".join(line).ljust(maxWidth))
        return res
