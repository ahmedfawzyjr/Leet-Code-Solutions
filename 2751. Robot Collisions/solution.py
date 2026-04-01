from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        indices = sorted(range(n), key=lambda i: positions[i])
        stack = [] # indexes of robots currently moving to the right
        
        # We need a copy of healths to modify during collisions
        # and eventually return in the original order.
        res_healths = list(healths)
        
        for i in indices:
            if directions[i] == 'R':
                stack.append(i)
            else:
                # current robot moves to the left ('L')
                while stack and res_healths[i] > 0:
                    top_idx = stack[-1]
                    if res_healths[top_idx] < res_healths[i]:
                        # Right-moving robot has less health, it gets removed
                        res_healths[i] -= 1
                        res_healths[top_idx] = 0
                        stack.pop()
                    elif res_healths[top_idx] > res_healths[i]:
                        # Left-moving robot has less health, it gets removed
                        res_healths[top_idx] -= 1
                        res_healths[i] = 0
                    else:
                        # Both have same health, both get removed
                        res_healths[i] = 0
                        res_healths[top_idx] = 0
                        stack.pop()
        
        return [h for h in res_healths if h > 0]
