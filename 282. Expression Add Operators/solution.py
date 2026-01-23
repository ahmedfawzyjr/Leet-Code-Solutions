from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        if not num:
            return res
        
        def backtrack(idx, path, current_val, last_val):
            if idx == len(num):
                if current_val == target:
                    res.append(path)
                return
            
            for i in range(idx, len(num)):
                # Leading zero check
                if i > idx and num[idx] == '0':
                    break
                
                sub_str = num[idx:i+1]
                val = int(sub_str)
                
                if idx == 0:
                    backtrack(i + 1, sub_str, val, val)
                else:
                    # Addition
                    backtrack(i + 1, path + "+" + sub_str, current_val + val, val)
                    # Subtraction
                    backtrack(i + 1, path + "-" + sub_str, current_val - val, -val)
                    # Multiplication
                    backtrack(i + 1, path + "*" + sub_str, current_val - last_val + last_val * val, last_val * val)
        
        backtrack(0, "", 0, 0)
        return res
