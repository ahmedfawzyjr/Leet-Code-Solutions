class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        max_len = 0
        
        for line in input.split('\n'):
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            
            while len(stack) > depth:
                stack.pop()
            
            if '.' in name:
                current_len = sum(stack) + len(stack) + len(name)
                max_len = max(max_len, current_len)
            else:
                stack.append(len(name))
                
        return max_len
