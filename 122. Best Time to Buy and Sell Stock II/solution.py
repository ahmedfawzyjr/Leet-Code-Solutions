from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    prices1 = [7,1,5,3,6,4]
    output1 = solution.maxProfit(prices1)
    print(f"Example 1: Input: prices = {prices1}, Output: {output1}")
    assert output1 == 7
    
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
