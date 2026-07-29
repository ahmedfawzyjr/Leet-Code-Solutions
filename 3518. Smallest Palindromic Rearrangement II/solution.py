class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        from collections import Counter
        import math

        counts = Counter(s)
        left_counts = {}
        mid_char = ""
        for c, count in counts.items():
            if count % 2 == 1:
                mid_char = c
            left_counts[c] = count // 2
            
        chars = sorted(left_counts.keys())
        left_char_counts = [left_counts[c] for c in chars]
        m = sum(left_char_counts)
        
        def count_ways(total_len, counts_list):
            num = math.factorial(total_len)
            den = 1
            for c in counts_list:
                if c > 1:
                    den *= math.factorial(c)
            return num // den
            
        initial_ways = count_ways(m, left_char_counts)
        if k > initial_ways:
            return ""
            
        left_half = []
        W = initial_ways
        
        for i in range(m):
            R = m - i
            for idx, c in enumerate(chars):
                if left_char_counts[idx] > 0:
                    ways = (W * left_char_counts[idx]) // R
                    if k > ways:
                        k -= ways
                    else:
                        left_half.append(c)
                        left_char_counts[idx] -= 1
                        W = ways
                        break
                        
        left_half_str = "".join(left_half)
        return left_half_str + mid_char + left_half_str[::-1]
