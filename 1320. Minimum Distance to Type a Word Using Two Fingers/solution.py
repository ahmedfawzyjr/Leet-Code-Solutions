class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_dist(a, b):
            if a is None or b is None:
                return 0
            idx1 = ord(a) - ord('A')
            idx2 = ord(b) - ord('A')
            x1, y1 = divmod(idx1, 6)
            x2, y2 = divmod(idx2, 6)
            return abs(x1 - x2) + abs(y1 - y2)

        from functools import lru_cache

        @lru_cache(None)
        def solve(index, other_finger):
            if index == len(word):
                return 0
            
            curr = word[index]
            prev = word[index-1]
            
            # Option 1: Move the finger that typed the previous character
            res1 = get_dist(prev, curr) + solve(index + 1, other_finger)
            
            # Option 2: Move the other finger (it was at 'other_finger' position)
            res2 = get_dist(other_finger, curr) + solve(index + 1, prev)
            
            return min(res1, res2)

        # Start with the first finger at word[0] (0 distance for first character)
        # Second finger is 'None' (available to be placed anywhere for 0 cost)
        return solve(1, None)
