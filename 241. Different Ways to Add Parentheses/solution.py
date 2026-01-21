from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        """
        Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.
        The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 10^4.
        """
        memo = {}

        def compute(expr):
            if expr in memo:
                return memo[expr]
            
            res = []
            for i, char in enumerate(expr):
                if char in "+-*":
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])
                    
                    for l in left:
                        for r in right:
                            if char == '+':
                                res.append(l + r)
                            elif char == '-':
                                res.append(l - r)
                            elif char == '*':
                                res.append(l * r)
            
            if not res:
                res.append(int(expr))
            
            memo[expr] = res
            return res

        return compute(expression)

if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    expression = "2-1-1"
    result = sol.diffWaysToCompute(expression)
    print(f"Expression: {expression}")
    print(f"Output: {sorted(result)} (Expected: [0, 2])")
    
    # Test Case 2
    expression = "2*3-4*5"
    result = sol.diffWaysToCompute(expression)
    print(f"Expression: {expression}")
    print(f"Output: {sorted(result)} (Expected: [-34, -14, -10, -10, 10])")
