class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return NestedInteger()
        
        if s[0] != '[':
            return NestedInteger(int(s))
        
        stack = []
        num = None
        sign = 1
        
        for i, char in enumerate(s):
            if char == '-':
                sign = -1
            elif char.isdigit():
                if num is None: num = 0
                num = num * 10 + int(char)
            elif char == '[':
                stack.append(NestedInteger())
            elif char == ',' or char == ']':
                if num is not None:
                    stack[-1].add(NestedInteger(sign * num))
                    num = None
                    sign = 1
                
                if char == ']' and len(stack) > 1:
                    last = stack.pop()
                    stack[-1].add(last)
        
        return stack[0]

if __name__ == "__main__":
    sol = Solution()
    print(sol.deserialize("324")) # Expected: 324
    print(sol.deserialize("[123,[456,[789]]]")) # Expected: [123,[456,[789]]]
    print(sol.deserialize("[]")) # Expected: []
