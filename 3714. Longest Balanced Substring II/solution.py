class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        # Case 1: Substrings with exactly 1 distinct character
        # (Any run of the same character is balanced)
        if n > 0:
            curr_len = 1
            for i in range(1, n):
                if s[i] == s[i-1]:
                    curr_len += 1
                else:
                    ans = max(ans, curr_len)
                    curr_len = 1
            ans = max(ans, curr_len)
            
        # Case 2: Substrings with exactly 2 distinct characters
        # For each pair of characters (X, Y), the substring must not contain the third character Z.
        # So we split the string by Z and find the longest substring with equal counts of X and Y.
        def solve2(char1, char2, other):
            res = 0
            segments = s.split(other)
            for seg in segments:
                if not seg:
                    continue
                # Longest substring with equal char1 and char2 counts (count > 0)
                diff_map = {0: -1}
                d = 0
                for i, c in enumerate(seg):
                    if c == char1:
                        d += 1
                    elif c == char2:
                        d -= 1
                    
                    if d in diff_map:
                        # If counts are equal, length is i - diff_map[d]
                        # In this segment of only char1 and char2, if length > 0,
                        # it guarantees both are present orCase 1 would have caught it if it was better.
                        # Actually, if length > 0 and d remains the same, it means 
                        # delta_char1 == delta_char2. Since only char1 and char2 are present, 
                        # a length L means k of char1 and k of char2, where 2k = L.
                        # If L > 0, then k > 0, so BOTH are present.
                        res = max(res, i - diff_map[d])
                    else:
                        diff_map[d] = i
            return res

        ans = max(ans, solve2('a', 'b', 'c'))
        ans = max(ans, solve2('b', 'c', 'a'))
        ans = max(ans, solve2('a', 'c', 'b'))
        
        # Case 3: Substrings with exactly 3 distinct characters
        # count(a) == count(b) == count(c)
        # This requires the prefix differences (da - db) and (db - dc) to be the same.
        diff_map = {(0, 0): -1}
        da, db, dc = 0, 0, 0
        for i, c in enumerate(s):
            if c == 'a':
                da += 1
            elif c == 'b':
                db += 1
            elif c == 'c':
                dc += 1
            
            key = (da - db, db - dc)
            if key in diff_map:
                # Same logic: if da, db, dc all increase by k, then k of each is added.
                # If i - prev_i > 0, k must be > 0, so all 3 are present.
                ans = max(ans, i - diff_map[key])
            else:
                diff_map[key] = i
                
        return ans

if __name__ == "__main__":
    sol = Solution()
    
    # Test cases from the problem description
    test_cases = [
        ("abbac", 4),
        ("aabcc", 3),
        ("aba", 2),
    ]
    
    for s, expected in test_cases:
        result = sol.longestBalanced(s)
        print(f"Input: s = \"{s}\"")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print("-" * 20)
