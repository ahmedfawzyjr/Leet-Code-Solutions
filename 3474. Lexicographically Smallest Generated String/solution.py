class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        L = n + m - 1
        word = ["?"] * L
        
        # 1. Apply 'T' constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    char = str2[j]
                    if word[i+j] != "?" and word[i+j] != char:
                        return ""
                    word[i+j] = char
        
        # 2. Pre-calculate q_count and is_mismatch for each window
        q_count = [0] * n
        is_mismatch = [False] * n
        for i in range(n):
            for k in range(m):
                if word[i+k] == "?":
                    q_count[i] += 1
                elif word[i+k] != str2[k]:
                    is_mismatch[i] = True
            
            # Initial 'F' violation check
            if str1[i] == 'F' and q_count[i] == 0 and not is_mismatch[i]:
                return ""
        
        # 3. Greedy filling for '?'
        for j in range(L):
            if word[j] == '?':
                forbidden = set()
                # A window i is at risk if it must not be str2 but currently has only one '?' left
                for i in range(max(0, j - m + 1), min(n, j + 1)):
                    if str1[i] == 'F' and not is_mismatch[i]:
                        if q_count[i] == 1:
                            forbidden.add(str2[j-i])
                
                # Pick smallest char satisfying all 'F' constraints
                found = False
                for char_code in range(ord('a'), ord('z') + 1):
                    c = chr(char_code)
                    if c not in forbidden:
                        word[j] = c
                        found = True
                        break
                if not found:
                    return ""
                
                # Update all windows containing this newly filled position
                for i in range(max(0, j - m + 1), min(n, j + 1)):
                    q_count[i] -= 1
                    if word[j] != str2[j-i]:
                        is_mismatch[i] = True
            else:
                # If word[j] was already fixed by 'T', it was accounted for in pre-calculation,
                # but windows i where i+k == j might still need its q_count/is_mismatch status.
                # Actually, they are already correct from the pre-calculation step.
                pass
                
        return "".join(word)

if __name__ == "__main__":
    sol = Solution()
    # Test cases
    print(f'Example 1: {sol.generateString("TFTF", "ab")}')  # Expected: "ababa"
    print(f'Example 2: {sol.generateString("TFTF", "abc")}') # Expected: ""
    print(f'Example 3: {sol.generateString("F", "d")}')      # Expected: "a"
