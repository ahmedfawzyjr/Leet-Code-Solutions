from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        """
        Calculates the minimum moves to collect all litter in the classroom using BFS with bitmask state.
        
        State representation: (r, c, mask, cur_energy)
        Pruning optimization: max_e[r][c][mask] stores the maximum remaining energy seen for state (r, c, mask).
        """
        m = len(classroom)
        n = len(classroom[0])
        
        start_r, start_c = -1, -1
        litters = {}
        
        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]
                if ch == 'S':
                    start_r, start_c = r, c
                elif ch == 'L':
                    litters[(r, c)] = len(litters)
                    
        num_litters = len(litters)
        if num_litters == 0:
            return 0
            
        target_mask = (1 << num_litters) - 1
        
        # max_e[r][c][mask] tracks maximum energy achieved at (r, c) with subset of litters collected
        max_e = [[[-1] * (1 << num_litters) for _ in range(n)] for _ in range(m)]
        
        q = deque()
        q.append((start_r, start_c, 0, energy, 0))
        max_e[start_r][start_c][0] = energy
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while q:
            r, c, mask, e, moves = q.popleft()
            
            if e <= 0:
                continue
                
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    ch = classroom[nr][nc]
                    if ch == 'X':
                        continue
                    
                    ne = e - 1
                    nmask = mask
                    
                    if ch == 'R':
                        ne = energy
                    elif ch == 'L':
                        litter_id = litters.get((nr, nc))
                        if litter_id is not None:
                            nmask = mask | (1 << litter_id)
                            if nmask == target_mask:
                                return moves + 1
                    
                    # If remaining energy is 0 and not at 'R', student cannot make any future moves
                    if ne == 0:
                        continue
                        
                    if ne > max_e[nr][nc][nmask]:
                        max_e[nr][nc][nmask] = ne
                        q.append((nr, nc, nmask, ne, moves + 1))
                        
        return -1


if __name__ == "__main__":
    sol = Solution()
    # Example 1: classroom = ["S.", "XL"], energy = 2 -> 2
    print(sol.minMoves(["S.", "XL"], 2))
    
    # Example 2: classroom = ["LS", "RL"], energy = 4 -> 3
    print(sol.minMoves(["LS", "RL"], 4))
    
    # Example 3: classroom = ["L.S", "RXL"], energy = 2 -> -1
    print(sol.minMoves(["L.S", "RXL"], 2))
