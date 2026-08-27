class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        x = y = 0
        moves = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0),
        }

        for direction in path:
            dx, dy = moves[direction]
            x += dx
            y += dy
            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False
