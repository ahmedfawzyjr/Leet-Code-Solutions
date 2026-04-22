from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for query in queries:
            for word in dictionary:
                # Count differences (Hamming distance)
                diff = 0
                for char_q, char_w in zip(query, word):
                    if char_q != char_w:
                        diff += 1
                    if diff > 2:
                        break
                
                if diff <= 2:
                    ans.append(query)
                    break
        return ans
