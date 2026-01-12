from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            if total_tank < 0:
                start_index = i + 1
                total_tank = 0
                
        return start_index

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    gas1 = [1,2,3,4,5]
    cost1 = [3,4,5,1,2]
    assert solution.canCompleteCircuit(gas1, cost1) == 3, f"Test case 1 failed: {solution.canCompleteCircuit(gas1, cost1)}"
    print("Test case 1 passed")
    
    # Example 2
    gas2 = [2,3,4]
    cost2 = [3,4,3]
    assert solution.canCompleteCircuit(gas2, cost2) == -1, f"Test case 2 failed: {solution.canCompleteCircuit(gas2, cost2)}"
    print("Test case 2 passed")
