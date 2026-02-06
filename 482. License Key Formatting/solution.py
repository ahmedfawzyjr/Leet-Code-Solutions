class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        n = len(s)
        
        first_group_len = n % k
        if first_group_len == 0:
            first_group_len = k if n > 0 else 0
            
        res = []
        if first_group_len > 0:
            res.append(s[:first_group_len])
            
        for i in range(first_group_len, n, k):
            res.append(s[i:i+k])
            
        return "-".join(res)
