from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        # Count frequency of each character
        count = Counter(s)
        
        # Digits mapping
        # 0: zero (z)
        # 2: two (w)
        # 4: four (u)
        # 6: six (x)
        # 8: eight (g)
        # 3: three (h - 8)
        # 5: five (f - 4)
        # 7: seven (s - 6)
        # 1: one (o - 0 - 2 - 4)
        # 9: nine (i - 5 - 6 - 8)
        
        res = [0] * 10
        res[0] = count['z']
        res[2] = count['w']
        res[4] = count['u']
        res[6] = count['x']
        res[8] = count['g']
        res[3] = count['h'] - res[8]
        res[5] = count['f'] - res[4]
        res[7] = count['s'] - res[6]
        res[1] = count['o'] - res[0] - res[2] - res[4]
        res[9] = count['i'] - res[5] - res[6] - res[8]
        
        output = []
        for i in range(10):
            output.append(str(i) * res[i])
            
        return "".join(output)
