from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Division between two integers always truncates toward zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
                
        return stack[0]

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    # ["2","1","+","3","*"]
    # Output: 9
    # ((2 + 1) * 3) = 9
    tokens1 = ["2","1","+","3","*"]
    print(f"Test Case 1: {solution.evalRPN(tokens1)} (Expected: 9)")
    
    # Test case 2
    # ["4","13","5","/","+"]
    # Output: 6
    # (4 + (13 / 5)) = 6
    tokens2 = ["4","13","5","/","+"]
    print(f"Test Case 2: {solution.evalRPN(tokens2)} (Expected: 6)")
    
    # Test case 3
    # ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    # Output: 22
    tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(f"Test Case 3: {solution.evalRPN(tokens3)} (Expected: 22)")
