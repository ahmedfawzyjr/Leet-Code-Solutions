class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        c0 = s.count('0')
        L, R = c0, c0
        ops = 0
        visited = set()
        
        while L <= R:
            if L <= 0 <= R and (L % 2 == 0):
                return ops
            
            if (L, R) in visited:
                break
            visited.add((L, R))
            
            # update L and R
            if k < L:
                L_next = L - k
            elif k > R:
                L_next = k - R
            elif k % 2 == L % 2:
                L_next = 0
            else:
                L_next = 1
                
            M = n - k
            if M < L:
                R_next = n - (L - M)
            elif M > R:
                R_next = n - (M - R)
            elif M % 2 == L % 2:
                R_next = n
            else:
                R_next = n - 1
                
            L, R = L_next, R_next
            ops += 1
            
        return -1
