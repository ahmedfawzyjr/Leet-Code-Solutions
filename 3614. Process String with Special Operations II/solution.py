
from collections import deque

class Solution:
    def processString(self, s: str, k: int) -> str:
        left = deque()
        right = deque()
        reversed_flag = False
        
        for c in s:
            if c.islower():
                if not reversed_flag:
                    right.append(c)
                else:
                    left.append(c)
            elif c == '-':
                if not reversed_flag:
                    if right:
                        right.pop()
                    elif left:
                        left.popleft()
                else:
                    if left:
                        left.pop()
                    elif right:
                        right.popleft()
            elif c == '+':
                if not reversed_flag:
                    last = right[-1] if right else left[0]
                    right.append(last)
                else:
                    last = left[-1] if left else right[0]
                    left.append(last)
            elif c == '!':
                reversed_flag = not reversed_flag
        
        # Build final string
        if not reversed_flag:
            final = list(left)[::-1] + list(right)
        else:
            final = list(right)[::-1] + list(left)
        
        return final[k]
