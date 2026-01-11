from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        buy1 = float('inf')
        profit1 = 0
        buy2 = float('inf')
        profit2 = 0
        
        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)
            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)
            
        return profit2

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    prices1 = [3,3,5,0,0,3,1,4]
    output1 = solution.maxProfit(prices1)
    print(f"Example 1: Input: prices = {prices1}, Output: {output1}")
    assert output1 == 6
    
    # Example 2
    prices2 = [1,2,3,4,5]
    output2 = solution.maxProfit(prices2)
    print(f"Example 2: Input: prices = {prices2}, Output: {output2}")
    assert output2 == 4
    
    # Example 3
    prices3 = [7,6,4,3,1]
    output3 = solution.maxProfit(prices3)
    print(f"Example 3: Input: prices = {prices3}, Output: {output3}")
    assert output3 == 0

    print("All test cases passed!")
