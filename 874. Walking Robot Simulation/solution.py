class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # Direction vectors: North, East, South, West
        dx: list[int] = [0, 1, 0, -1]
        dy: list[int] = [1, 0, -1, 0]
        
        # Initial state
        x, y = 0, 0
        d: int = 0  # 0: North, 1: East, 2: South, 3: West
        
        # Convert obstacles to a set for O(1) lookup
        obstacle_set: set[tuple[int, int]] = set(map(lambda o: (o[0], o[1]), obstacles))
        
        max_dist_sq: int = 0
        
        for cmd in commands:
            if cmd == -2:  # Turn left
                d = (d - 1) % 4
            elif cmd == -1:  # Turn right
                d = (d + 1) % 4
            else:  # Move forward cmd units
                for _ in range(cmd):
                    curr_dx, curr_dy = dx[d], dy[d]
                    nx, ny = x + curr_dx, y + curr_dy
                    if (nx, ny) not in (obstacle_set):
                        x, y = nx, ny
                        max_dist_sq = max(max_dist_sq, x*x + y*y)
                    else:
                        break
        
        return max_dist_sq
