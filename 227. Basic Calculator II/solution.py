class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        stack = []
        current_num = 0
        operation = '+'
        s += '+' # Append a dummy operator to trigger the last calculation
        
        for i, char in enumerate(s):
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            
            if char in "+-*/" or i == len(s) - 1:
                if operation == '+':
                    stack.append(current_num)
                elif operation == '-':
                    stack.append(-current_num)
                elif operation == '*':
                    stack.append(stack.pop() * current_num)
                elif operation == '/':
                    # Integer division truncating toward zero
                    top = stack.pop()
                    if top < 0:
                        stack.append(-(-top // current_num))
                    else:
                        stack.append(top // current_num)
                
                operation = char
                current_num = 0
                
        return sum(stack)

if __name__ == "__main__":
    sol = Solution()
    print(f"3+2*2 = {sol.calculate('3+2*2')}") # 7
    print(f" 3/2  = {sol.calculate(' 3/2 ')}") # 1
    print(f" 3+5 / 2  = {sol.calculate(' 3+5 / 2 ')}") # 5
