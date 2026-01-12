from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        
        # Left to right
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
                
        # Right to left
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
                
        return sum(candies)

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    ratings1 = [1,0,2]
    assert solution.candy(ratings1) == 5, f"Test case 1 failed: {solution.candy(ratings1)}"
    print("Test case 1 passed")
    
    # Example 2
    ratings2 = [1,2,2]
    assert solution.candy(ratings2) == 4, f"Test case 2 failed: {solution.candy(ratings2)}"
    print("Test case 2 passed")
