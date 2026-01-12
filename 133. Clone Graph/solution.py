from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}
        
        def dfs(curr_node):
            if curr_node in visited:
                return visited[curr_node]
            
            clone_node = Node(curr_node.val)
            visited[curr_node] = clone_node
            
            if curr_node.neighbors:
                for neighbor in curr_node.neighbors:
                    clone_node.neighbors.append(dfs(neighbor))
            
            return clone_node
        
        return dfs(node)

if __name__ == "__main__":
    solution = Solution()
    
    # Helper to build graph from adjacency list
    def build_graph(adj_list):
        if not adj_list:
            return None
        nodes = [Node(i + 1) for i in range(len(adj_list))]
        for i, neighbors in enumerate(adj_list):
            for neighbor_idx in neighbors:
                nodes[i].neighbors.append(nodes[neighbor_idx - 1])
        return nodes[0]

    # Helper to convert graph to adjacency list for verification
    def get_adj_list(node):
        if not node:
            return []
        visited = {}
        result = {}
        queue = [node]
        visited[node.val] = node
        
        while queue:
            curr = queue.pop(0)
            result[curr.val] = [n.val for n in curr.neighbors]
            for n in curr.neighbors:
                if n.val not in visited:
                    visited[n.val] = n
                    queue.append(n)
        
        sorted_keys = sorted(result.keys())
        final_adj = []
        for k in sorted_keys:
            final_adj.append(result[k])
        return final_adj

    # Example 1
    adj1 = [[2,4],[1,3],[2,4],[1,3]]
    node1 = build_graph(adj1)
    cloned1 = solution.cloneGraph(node1)
    assert get_adj_list(cloned1) == adj1, "Test case 1 failed"
    print("Test case 1 passed")
    
    # Example 2
    adj2 = [[]]
    node2 = build_graph(adj2)
    cloned2 = solution.cloneGraph(node2)
    assert get_adj_list(cloned2) == adj2, "Test case 2 failed"
    print("Test case 2 passed")
    
    # Example 3
    adj3 = []
    node3 = build_graph(adj3)
    cloned3 = solution.cloneGraph(node3)
    assert get_adj_list(cloned3) == adj3, "Test case 3 failed"
    print("Test case 3 passed")
