from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list and in-degree array
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
            
        # Initialize queue with courses having 0 in-degree
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []
        
        while queue:
            course = queue.popleft()
            result.append(course)
            
            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # Check if all courses are possible
        if len(result) == numCourses:
            return result
        else:
            return []

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    numCourses = 2
    prerequisites = [[1,0]]
    print(f"Example 1: {sol.findOrder(numCourses, prerequisites)}") # Expected: [0, 1]
    
    # Example 2
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(f"Example 2: {sol.findOrder(numCourses, prerequisites)}") # Expected: [0, 1, 2, 3] or [0, 2, 1, 3]
    
    # Example 3
    numCourses = 1
    prerequisites = []
    print(f"Example 3: {sol.findOrder(numCourses, prerequisites)}") # Expected: [0]
