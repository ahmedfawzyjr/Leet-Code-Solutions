from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
            
        itinerary = []
        
        def dfs(airport):
            while adj[airport]:
                next_airport = adj[airport].pop()
                dfs(next_airport)
            itinerary.append(airport)
            
        dfs("JFK")
        return itinerary[::-1]

if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    tickets1 = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    print(f"Example 1: {sol.findItinerary(tickets1)}") # Expected: ["JFK","MUC","LHR","SFO","SJC"]
    
    # Example 2
    tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print(f"Example 2: {sol.findItinerary(tickets2)}") # Expected: ["JFK","ATL","JFK","SFO","ATL","SFO"]
