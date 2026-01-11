from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    prices1 = [7,1,5,3,6,4]
    output1 = solution.maxProfit(prices1)
    print(f"Example 1: Input: prices = {prices1}, Output: {output1}")
    assert output1 == 5
    
    # Example 2
    prices2 = [7,6,4,3,1]
    output2 = solution.maxProfit(prices2)
    print(f"Example 2: Input: prices = {prices2}, Output: {output2}")
    assert output2 == 0
    
    print("All test cases passed!")
