from collections import Counter


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        """
        Returns the lexicographically smallest palindromic permutation of s
        that is strictly greater than target. If no such permutation exists,
        returns an empty string.
        """
        n = len(s)
        counts = Counter(s)
        
        # Check if a palindromic permutation of s can be formed
        odd_chars = [c for c, cnt in counts.items() if cnt % 2 == 1]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        left_counts = {c: counts[c] // 2 for c in counts}
        m = n // 2
        T_left = target[:m]
        
        def make_palindrome(left_half: str) -> str:
            return left_half + mid_char + left_half[::-1]
        
        # Case 1: Try using T_left directly as the left half
        t_left_counts = Counter(T_left)
        if all(t_left_counts[c] == left_counts.get(c, 0) for c in t_left_counts) and sum(t_left_counts.values()) == m:
            candidate = make_palindrome(T_left)
            if candidate > target:
                return candidate
        
        # Case 2: Find the lexicographically smallest left half L strictly greater than T_left
        # Precompute prefix character counts of T_left
        pref = [Counter()]
        for ch in T_left:
            c_copy = pref[-1].copy()
            c_copy[ch] += 1
            pref.append(c_copy)
        
        # Find maximum valid prefix length of T_left formed by left_counts
        cur_counts = Counter()
        valid_prefix_len = 0
        for ch in T_left:
            cur_counts[ch] += 1
            if cur_counts[ch] > left_counts.get(ch, 0):
                break
            valid_prefix_len += 1
        
        # Search from longest common prefix downwards
        for i in range(min(m - 1, valid_prefix_len), -1, -1):
            used = pref[i]
            rem = {c: left_counts[c] - used.get(c, 0) for c in left_counts}
            target_char = target[i]
            
            # Find the smallest available character c > target[i]
            cand_c = None
            for char_code in range(ord(target_char) + 1, ord("z") + 1):
                ch = chr(char_code)
                if rem.get(ch, 0) > 0:
                    cand_c = ch
                    break
            
            if cand_c is not None:
                rem[cand_c] -= 1
                suffix = []
                for char_code in range(ord("a"), ord("z") + 1):
                    ch = chr(char_code)
                    if rem.get(ch, 0) > 0:
                        suffix.append(ch * rem[ch])
                
                L = T_left[:i] + cand_c + "".join(suffix)
                return make_palindrome(L)
        
        return ""
