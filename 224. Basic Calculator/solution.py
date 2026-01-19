class Solution:
    def calculate(self, s: str) -> int:
        """
        Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
        
        Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
        
        Constraints:
        - s consists of digits, '+', '-', '(', ')', and ' '.
        - s represents a valid expression.
        - '+' is not used as a unary operation.
        - '-' could be used as a unary operation.
        - There will be no two consecutive operators in the input.
        - Every number and running calculation will fit in a signed 32-bit integer.
        
        Approach:
        Use a stack to handle parentheses.
        Maintain current result, current sign, and current number.
        """
        stack = []
        current_result = 0
        current_num = 0
        sign = 1  # 1 for positive, -1 for negative
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '+':
                current_result += sign * current_num
                current_num = 0
                sign = 1
            elif char == '-':
                current_result += sign * current_num
                current_num = 0
                sign = -1
            elif char == '(':
                # Push current result and sign onto stack
                stack.append(current_result)
                stack.append(sign)
                # Reset result and sign for the sub-expression
                current_result = 0
                sign = 1
            elif char == ')':
                current_result += sign * current_num
                current_num = 0
                # Pop sign and previous result
                prev_sign = stack.pop()
                prev_result = stack.pop()
                current_result = prev_result + prev_sign * current_result
            # Ignore spaces
            
        current_result += sign * current_num
        return current_result
