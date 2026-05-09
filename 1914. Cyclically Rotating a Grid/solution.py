from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        num_layers = min(m, n) // 2
        
        for layer in range(num_layers):
            # Extract the layer elements in counter-clockwise order
            layer_elements = []
            
            # Left column: (layer, layer) to (m-1-layer, layer)
            for i in range(layer, m - layer):
                layer_elements.append(grid[i][layer])
            
            # Bottom row: (m-1-layer, layer+1) to (m-1-layer, n-1-layer)
            for j in range(layer + 1, n - layer):
                layer_elements.append(grid[m - 1 - layer][j])
            
            # Right column: (m-2-layer, n-1-layer) to (layer, n-1-layer)
            for i in range(m - 2 - layer, layer - 1, -1):
                layer_elements.append(grid[i][n - 1 - layer])
            
            # Top row: (layer, n-2-layer) to (layer, layer+1)
            for j in range(n - 2 - layer, layer, -1):
                layer_elements.append(grid[layer][j])
            
            # Calculate effective rotation
            size = len(layer_elements)
            rot = k % size
            
            # Rotate layer_elements counter-clockwise by k
            # In our list, counter-clockwise is moving towards higher indices.
            # However, the problem says "each element in the layer will take the place of the adjacent element in the counter-clockwise direction".
            # This means the element at index i moves to index (i + 1) % size.
            # If we rotate k times, element at index i moves to (i + k) % size.
            # So the new list will have the element that was at (i - k) % size at index i.
            
            rotated_layer = [0] * size
            for i in range(size):
                rotated_layer[(i + rot) % size] = layer_elements[i]
            
            # Put back into the grid
            idx = 0
            for i in range(layer, m - layer):
                grid[i][layer] = rotated_layer[idx]
                idx += 1
            for j in range(layer + 1, n - layer):
                grid[m - 1 - layer][j] = rotated_layer[idx]
                idx += 1
            for i in range(m - 2 - layer, layer - 1, -1):
                grid[i][n - 1 - layer] = rotated_layer[idx]
                idx += 1
            for j in range(n - 2 - layer, layer, -1):
                grid[layer][j] = rotated_layer[idx]
                idx += 1
                
        return grid

if __name__ == "__main__":
    s = Solution()
    
    # Test case 1
    grid1 = [[40, 10], [30, 20]]
    k1 = 1
    print(s.rotateGrid(grid1, k1)) # Expected: [[10, 20], [40, 30]]
    
    # Test case 2
    grid2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    k2 = 2
    print(s.rotateGrid(grid2, k2)) # Expected: [[3, 4, 8, 12], [2, 11, 10, 16], [1, 7, 6, 15], [5, 13, 14, 15]] - wait, let me re-check example 2
