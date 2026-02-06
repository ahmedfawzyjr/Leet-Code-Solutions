import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        
        # n = k^m + k^(m-1) + ... + k + 1
        # n = (k^(m+1) - 1) / (k - 1)
        # We want the smallest k, which means we should try the largest m.
        # Max m can be found when k is smallest (k=2). 2^(m+1) - 1 = n => m ~ log2(n)
        
        max_m = int(math.log2(num))
        
        for m in range(max_m, 1, -1):
            # Try to find k such that (k^(m+1) - 1) / (k-1) = num
            # k^m < num < (k+1)^m (roughly)
            # So k ~ num^(1/m)
            k = int(num**(1/m))
            
            if k > 1:
                # Geometric sum: k^m + k^(m-1) + ... + 1
                total = 0
                for i in range(m + 1):
                    total = total * k + 1
                
                if total == num:
                    return str(k)
                    
        return str(num - 1)
