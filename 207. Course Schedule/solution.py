from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list and in-degree array
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
            
        # Initialize queue with courses having 0 in-degree
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0
        
        while queue:
            course = queue.popleft()
            count += 1
            
            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return count == numCourses

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    numCourses = 2
    prerequisites = [[1,0]]
    print(f"Example 1: {sol.canFinish(numCourses, prerequisites)}") # Expected: True
    
    # Example 2
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print(f"Example 2: {sol.canFinish(numCourses, prerequisites)}") # Expected: False
