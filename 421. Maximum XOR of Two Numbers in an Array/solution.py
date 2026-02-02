from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Trie approach or bit manipulation with prefixes
        # Using bit manipulation with prefixes for conciseness
        max_xor = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            prefixes = {num & mask for num in nums}
            
            # Try to see if we can set the i-th bit to 1
            target = max_xor | (1 << i)
            for p in prefixes:
                if (target ^ p) in prefixes:
                    max_xor = target
                    break
        return max_xor
